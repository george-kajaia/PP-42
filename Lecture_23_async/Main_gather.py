import asyncio

base_url = "https://example.com/api/data"

async def fetch(url):
    await asyncio.sleep(1)
    return f"Fetched data from {url}"


async def main():
    return await asyncio.gather(
    fetch(base_url), 
    fetch(base_url),
    fetch(base_url))

if __name__ == "__main__":
    results = asyncio.run(main())

    for i in range(len(results)):
        print(results[i])
