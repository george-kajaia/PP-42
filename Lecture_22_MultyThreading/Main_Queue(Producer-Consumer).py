###----Queue: Producer-Consumer ---------------------------------------------------------------------

import queue, threading

def producer(queue, items):
    for item in items:
        queue.put(item)
    queue.put(None) # sentinel to signal done

def consumer(queue, results):
    while True:
        item = queue.get()
        if item is None:
            break
        results.append(item * 2)


main_queue = queue.Queue()
results = []
items = list(range(10))

t1 = threading.Thread(target=producer, args=(main_queue, items))
t2 = threading.Thread(target=consumer, args=(main_queue, results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)

###-------------------------------------------------------------------------

import concurrent.futures, time, random
from concurrent.futures import as_completed

def fetch(url):
    time.sleep(random.uniform(0.1, 1.0)) # simulate variable latency
    return f"data from {url}"

urls =[f"https://api.example.com/item/{i}" for i in range(5)]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(fetch,url): url for url in urls}   

    for future in as_completed(futures):        
        url = futures[future]
        try:
            result = future.result()
            print(f"✓ {url}: {result}")
        except Exception as e:
            print(f"✗ {url} failed: {e}")