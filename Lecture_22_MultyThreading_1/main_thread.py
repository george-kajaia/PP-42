import threading
import time



# def task(name, duration):
#     print(f"[{name}] starting")
#     time.sleep(duration)
#     print(f"[{name}] done after {duration}s")

# t1 = threading.Thread(target=task, args=("Thread-1", 2))
# t2 = threading.Thread(target=task, args=("Thread-2", 3))

# time1 = time.time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# time1 = time.time() - time1

# print(f"Total time taken: {time1:.2f}s")
# print("--------------------------------")

# time1 = time.time()
# task("Thread-1", 2)
# task("Thread-2", 3)
# time1 = time.time() - time1
# print(f"Total time taken: {time1:.2f}s")



# counter = 0

# def increment():
#     global counter
#     time.sleep(3)
#     for _ in range(100_000):
#         counter += 1

# threads = [threading.Thread(target=increment) for _ in range(5)]
# for t in threads: 
#     t.start()

# for t in threads: 
#         t.join()

# print(counter)


counter = 0

lock = threading.Lock()
def increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1
threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: 
        t.start()

for t in threads: 
        t.join()

print(counter)
