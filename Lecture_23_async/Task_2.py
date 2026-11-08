import asyncio
import aiohttp

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Fetch One Post
async def fetch_post(session, post_id):
    async with session.get(f"{BASE_URL}/{post_id}") as response:
        response.raise_for_status()
        return await response.json()


# Fetch 20 Posts Asynchronously
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post(session, i) for i in range(1, 21)]
        posts = await asyncio.gather(*tasks)

        filtered_posts = filter(lambda x: x["userId"] == 1, posts)      

        print(filtered_posts, "\n")
        for post in filtered_posts:
            print(post["title"])

if __name__ == "__main__":
    asyncio.run(main())