import asyncio

base_url = "https://example.com/api/data"

async def fetch(url):
    await asyncio.sleep(1)
    return f"Fetched data from {url}"


async def main():
    t1 = asyncio.create_task(fetch(base_url))
    t2 = asyncio.create_task(fetch(base_url))
    t3 = asyncio.create_task(fetch(base_url))

    await t1
    await t2
    await t3

    return [t1, t2, t3]

if __name__ == "__main__":
    results = asyncio.run(main())

    for i in range(len(results)):
        print(results[i])
