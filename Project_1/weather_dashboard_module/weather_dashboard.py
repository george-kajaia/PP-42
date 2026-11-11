import asyncio
import sqlite3
import time
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import aiohttp
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = Path(__file__).resolve().parent / "weather_dashboard.db"
console = Console()


@contextmanager
def database():
    """Create, commit/rollback and close a fresh SQLite connection."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with database() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                UNIQUE(name, country, latitude, longitude)
            );

            CREATE TABLE IF NOT EXISTS weather_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_name TEXT NOT NULL,
                country TEXT NOT NULL,
                observed_at TEXT NOT NULL,
                timezone TEXT NOT NULL,
                temperature REAL NOT NULL,
                wind_speed REAL NOT NULL,
                weather_code INTEGER NOT NULL,
                saved_at_utc TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_weather_history_city
                ON weather_history(city_name, saved_at_utc DESC);
            """
        )


def list_saved_cities() -> list[City]:
    with database() as conn:
        rows = conn.execute(
            "SELECT id, name, country, latitude, longitude "
            "FROM cities ORDER BY name, country"
        ).fetchall()
    return [
        City(
            name=row["name"],
            country=row["country"],
            latitude=row["latitude"],
            longitude=row["longitude"],
            db_id=row["id"],
        )
        for row in rows
    ]


def save_city(city: City) -> bool:
    with database() as conn:
        cursor = conn.execute(
            "INSERT OR IGNORE INTO cities (name, country, latitude, longitude) "
            "VALUES (?, ?, ?, ?)",
            (city.name, city.country, city.latitude, city.longitude),
        )
        return cursor.rowcount > 0


def delete_city(city_id: int) -> bool:
    with database() as conn:
        cursor = conn.execute("DELETE FROM cities WHERE id = ?", (city_id,))
        return cursor.rowcount > 0


def save_weather(weather: Weather):
    with database() as conn:
        conn.execute(
            """
            INSERT INTO weather_history
                (city_name, country, observed_at, timezone, temperature,
                 wind_speed, weather_code, saved_at_utc)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                weather.city.name,
                weather.city.country,
                weather.observed_at,
                weather.timezone,
                weather.temperature,
                weather.wind_speed,
                weather.weather_code,
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
            ),
        )


def get_history(city_name: str = "", limit: int = 30):
    with database() as conn:
        if city_name:
            return conn.execute(
                """
                SELECT * FROM weather_history
                WHERE city_name = ? COLLATE NOCASE
                ORDER BY id DESC LIMIT ?
                """,
                (city_name, limit),
            ).fetchall()
        return conn.execute(
            "SELECT * FROM weather_history ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()


async def fetch_json(session: aiohttp.ClientSession, url: str, params: dict) -> dict:
    async with session.get(url, params=params) as response:
        response.raise_for_status()
        payload = await response.json()
    if payload.get("error"):
        raise ValueError(payload.get("reason", "API-მ შეცდომა დააბრუნა"))
    return payload


async def find_city(session: aiohttp.ClientSession, name: str) -> City:
    payload = await fetch_json(
        session,
        GEOCODING_URL,
        {"name": name, "count": 1, "language": "ka"},
    )
    results = payload.get("results") or []
    if not results:
        raise ValueError(f"ქალაქი ვერ მოიძებნა: {name}")
    item = results[0]
    return City(
        name=item["name"],
        country=item.get("country", "უცნობი ქვეყანა"),
        latitude=float(item["latitude"]),
        longitude=float(item["longitude"]),
    )


async def fetch_weather(session: aiohttp.ClientSession, city: City) -> Weather:
    payload = await fetch_json(
        session,
        WEATHER_URL,
        {
            "latitude": city.latitude,
            "longitude": city.longitude,
            "current": "temperature_2m,wind_speed_10m,weather_code",
            "timezone": "auto",
        },
    )
    current = payload["current"]
    return Weather(
        city=city,
        observed_at=current["time"],
        timezone=payload.get("timezone", "GMT"),
        temperature=float(current["temperature_2m"]),
        wind_speed=float(current["wind_speed_10m"]),
        weather_code=int(current["weather_code"]),
    )


def weather_description(code: int) -> str:
    descriptions = {
        0: "მოწმენდილი", 1: "უმეტესად მოწმენდილი", 2: "ნაწილობრივ ღრუბლიანი",
        3: "ღრუბლიანი", 45: "ნისლი", 48: "ყინვიანი ნისლი",
        51: "სუსტი ჟინჟღლი", 53: "ჟინჟღლი", 55: "ძლიერი ჟინჟღლი",
        56: "სუსტი გაყინული ჟინჟღლი", 57: "ძლიერი გაყინული ჟინჟღლი",
        61: "სუსტი წვიმა", 63: "წვიმა", 65: "ძლიერი წვიმა",
        66: "სუსტი გაყინული წვიმა", 67: "ძლიერი გაყინული წვიმა",
        71: "სუსტი თოვა", 73: "თოვა", 75: "ძლიერი თოვა",
        77: "თოვლის მარცვლები", 80: "სუსტი წვიმის შხაპი",
        81: "წვიმის შხაპი", 82: "ძლიერი წვიმის შხაპი",
        85: "სუსტი თოვის შხაპი", 86: "ძლიერი თოვის შხაპი",
        95: "ჭექა-ქუხილი", 96: "ჭექა-ქუხილი, სუსტი სეტყვა",
        99: "ჭექა-ქუხილი, ძლიერი სეტყვა",
    }
    return descriptions.get(code, f"უცნობი კოდი ({code})")


def display_weather(reports: list[Weather]):
    table = Table(title="🌤 ამინდის მიმდინარე მონაცემები", show_lines=True)
    table.add_column("ქალაქი", style="cyan")
    table.add_column("ქვეყანა")
    table.add_column("დრო (ადგილობრივი)")
    table.add_column("°C", justify="right", style="bold green")
    table.add_column("ქარი (კმ/სთ)", justify="right")
    table.add_column("ამინდი", style="magenta")
    for weather in reports:
        table.add_row(
            weather.city.name,
            weather.city.country,
            f"{weather.observed_at.replace('T', ' ')}\n{weather.timezone}",
            f"{weather.temperature:.1f}",
            f"{weather.wind_speed:.1f}",
            weather_description(weather.weather_code),
        )
    console.print(table)


def display_cities(cities: list[City]):
    if not cities:
        console.print("[yellow]ქალაქების სია ცარიელია.[/yellow]")
        return
    table = Table(title="შენახული ქალაქები")
    table.add_column("ID", justify="right")
    table.add_column("ქალაქი", style="cyan")
    table.add_column("ქვეყანა")
    table.add_column("განედი", justify="right")
    table.add_column("გრძედი", justify="right")
    for city in cities:
        table.add_row(
            str(city.db_id), city.name, city.country,
            f"{city.latitude:.4f}", f"{city.longitude:.4f}",
        )
    console.print(table)


def display_history(rows):
    if not rows:
        console.print("[yellow]ისტორიაში ჩანაწერები არ არის.[/yellow]")
        return
    table = Table(title="ამინდის ისტორია (ბოლო 30 ჩანაწერი)", show_lines=True)
    table.add_column("ქალაქი", style="cyan")
    table.add_column("გაზომვის დრო")
    table.add_column("შენახულია (UTC)")
    table.add_column("°C", justify="right")
    table.add_column("ქარი", justify="right")
    table.add_column("ამინდი")
    for row in rows:
        table.add_row(
            f"{row['city_name']}\n{row['country']}",
            f"{row['observed_at'].replace('T', ' ')}\n{row['timezone']}",
            row["saved_at_utc"].replace("T", " ").removesuffix("+00:00"),
            f"{row['temperature']:.1f}",
            f"{row['wind_speed']:.1f}",
            weather_description(row["weather_code"]),
        )
    console.print(table)


async def add_city_action(session: aiohttp.ClientSession):
    name = console.input("ქალაქის სახელი: ").strip()
    if not name:
        return
    try:
        city = await find_city(session, name)
        if save_city(city):
            console.print(f"[green]დაემატა: {city.name}, {city.country}[/green]")
        else:
            console.print("[yellow]ეს ქალაქი უკვე სიაშია.[/yellow]")
    except (aiohttp.ClientError, asyncio.TimeoutError, ValueError, KeyError, TypeError) as exc:
        console.print(f"[red]შეცდომა: {exc}[/red]")


async def single_city_action(session: aiohttp.ClientSession):
    name = console.input("ქალაქის სახელი: ").strip()
    if not name:
        return
    try:
        city = await find_city(session, name)
        weather = await fetch_weather(session, city)
        save_weather(weather)
        display_weather([weather])
    except (aiohttp.ClientError, asyncio.TimeoutError, ValueError, KeyError, TypeError) as exc:
        console.print(f"[red]შეცდომა: {exc}[/red]")


async def all_cities_action(session: aiohttp.ClientSession):
    cities = list_saved_cities()
    if not cities:
        console.print("[yellow]ჯერ დაამატეთ ერთი ქალაქი მაინც.[/yellow]")
        return

    started = time.perf_counter()
    # ყველა HTTP მოთხოვნა ერთდროულად იწყება; შედეგები იმავე თანმიმდევრობით ბრუნდება.
    results = await asyncio.gather(
        *(fetch_weather(session, city) for city in cities),
        return_exceptions=True,
    )
    elapsed = time.perf_counter() - started

    successes: list[Weather] = []
    for city, result in zip(cities, results):
        if isinstance(result, BaseException):
            console.print(f"[red]{city.name}: {result}[/red]")
        else:
            save_weather(result)
            successes.append(result)

    if successes:
        display_weather(successes)
    console.print(
        f"[bold]წარმატებით მიღებულია {len(successes)}/{len(cities)} ქალაქის ამინდი "
        f"{elapsed:.2f} წამში.[/bold]"
    )


def remove_city_action():
    cities = list_saved_cities()
    display_cities(cities)
    if not cities:
        return
    raw_id = console.input("წასაშლელი ქალაქის ID: ").strip()
    if not raw_id.isdecimal():
        console.print("[red]შეიყვანეთ რიცხვითი ID.[/red]")
        return
    if delete_city(int(raw_id)):
        console.print("[green]ქალაქი წაიშალა სიიდან; ისტორია შენარჩუნებულია.[/green]")
    else:
        console.print("[yellow]ამ ID-ით ქალაქი არ მოიძებნა.[/yellow]")


def history_action():
    name = console.input("ქალაქის სახელი (Enter = ყველა ქალაქი): ").strip()
    display_history(get_history(name))


async def main():
    initialize_database()
    timeout = aiohttp.ClientTimeout(total=15)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        while True:
            console.print(
                Panel(
                    "[bold]1[/bold]  ერთი ქალაქის ამინდი (სახელით)\n"
                    "[bold]2[/bold]  ქალაქის დამატება\n"
                    "[bold]3[/bold]  ქალაქის წაშლა\n"
                    "[bold]4[/bold]  შენახული ქალაქების ნახვა\n"
                    "[bold]5[/bold]  ყველა ქალაქის ამინდის პარალელურად მიღება\n"
                    "[bold]6[/bold]  ამინდის ისტორიის ნახვა\n"
                    "[bold]0[/bold]  გამოსვლა",
                    title="Asynchronous Weather Dashboard",
                    border_style="blue",
                )
            )
            choice = console.input("აირჩიეთ მოქმედება: ").strip()
            if choice == "1":
                await single_city_action(session)
            elif choice == "2":
                await add_city_action(session)
            elif choice == "3":
                remove_city_action()
            elif choice == "4":
                display_cities(list_saved_cities())
            elif choice == "5":
                await all_cities_action(session)
            elif choice == "6":
                history_action()
            elif choice == "0":
                console.print("[green]ნახვამდის![/green]")
                break
            else:
                console.print("[yellow]არასწორი არჩევანია.[/yellow]")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        console.print("\n[yellow]პროგრამა დასრულდა.[/yellow]")
