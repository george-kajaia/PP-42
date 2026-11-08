import requests
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    r = requests.get(url, timeout=10)
    return r.json()

urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 11)]


with ThreadPoolExecutor(max_workers=10) as executor:
    # results = list(executor.map(fetch, urls))
    results = [executor.submit(fetch, url) for url in urls]

    for x in concurrent.futures.as_completed(results):
        print(x)

    print(type(results))




# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     results = list(executor.submit(fetch, url) for url in urls)

#     print(type(results))

#     for x in results:
#         print(x.result())





# import time
# from concurrent.futures import ThreadPoolExecutor, as_completed

# def task(seconds):
#     time.sleep(seconds)
#     return seconds

# with ThreadPoolExecutor(max_workers=3) as executor:
#      futures = [executor.submit(task, seconds) for seconds in [4, 1, 2]]
#      results = list(executor.map(fetch, urls))
    
#      print(1111)

#     for future in as_completed(futures):
#         print(future.result())

#     for future in futures:
#         print(future.result())

