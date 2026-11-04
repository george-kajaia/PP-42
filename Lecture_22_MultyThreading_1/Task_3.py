
import requests
import time
from concurrent.futures import ThreadPoolExecutor


def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Post {post_id}: Status {response.status_code}")
        return response.status_code

    except requests.RequestException as e:
        print(f"Post {post_id}: Error - {e}")
        return None


start_time = time.time()

# Send 100 requests using a pool of 10 threads
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(get_post, range(1, 101)))

end_time = time.time()

print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")
print(f"Successful requests: {results.count(200)}")
