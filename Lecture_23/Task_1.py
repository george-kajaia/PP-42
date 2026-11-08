import requests
import aiohttp
import asyncio
import time

BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

# 1. Sequential requests
def sequential_requests():
    start_time = time.time()

    for i in range(1, 11):
        response = requests.get(f"{BASE_URL}{i}", timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"Sequential: {data['id']}")

    return time.time() - start_time


# 2. Asynchronous requests
async def fetch(session, i):
    async with session.get(f"{BASE_URL}{i}") as response:
        response.raise_for_status()
        data = await response.json()
        print(f"Async: {data['id']}")
        return data

async def asynchronous_requests():
    start_time = time.time()

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch(session, i) for i in range(1, 11)]
        await asyncio.gather(*tasks)

    return time.time() - start_time


if __name__ == "__main__":
    sequential_time = sequential_requests()
    print(f"\nSequential time: {sequential_time:.3f} seconds")

    asynchronous_time = asyncio.run(asynchronous_requests())
    print(f"\nAsynchronous time: {asynchronous_time:.3f} seconds")

    difference = sequential_time - asynchronous_time

    if difference > 0:
        print(f"\nასინქრონულმა ვერსიამ {difference:.3f} წამით უფრო სწრაფად იმუშავა")
    else:
        print(f"\nსინქრონულმა ვერსიამ {-difference:.3f} წამით უფრო სწრაფად იმუშავა")
