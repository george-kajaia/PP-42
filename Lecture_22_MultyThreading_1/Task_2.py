import threading
import requests
import time


def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Post {post_id}: Status {response.status_code}")
    except requests.RequestException as e:
        print(f"Post {post_id}: Error - {e}")


threads = []

start_time = time.time()

# Create and start 100 threads
for i in range(1, 101):
    thread = threading.Thread(target=get_post, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

end_time = time.time()

print(f"\nTotal execution time: {end_time - start_time:.4f} seconds")
