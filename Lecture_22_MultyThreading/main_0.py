# import sys
# print(sys.version)
# print(sys._is_gil_enabled())

# from concurrent.futures import ProcessPoolExecutor

# def calculate(n):
#     return sum(i * i for i in range(n))

# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results = list(executor.map(calculate, [10_000_000] * 4)
#         )

#     print(results)



# import threading
# import time

# def task():
#     time.sleep(2)

# start = time.time()

# threads = []

# for i in range(3):
#     t = threading.Thread(target=task)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print(time.time() - start)




# t1 = threading.Thread(target=task, args=())
# t2 = threading.Thread(target=task, args=())

# time1 = time.time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# print(f"Total time taken: {time.time() - time1:.2f}s")


# import example
# example.get_name()

# number = 11
# workers = 10

# chunk_size = number // workers
# if number % workers != 0:
#     print("Chunk size is not an integer, increasing chunk size by 1")
#     chunk_size += 1

# print(chunk_size)

# arguments = []
# for i in range(1, workers):   
#     start = chunk_size * (i - 1) + 1
#     end = start + chunk_size - 1
#     arguments.append([start, end])

# if end != number:    
#     arguments.append([end+1, number])

# print(arguments)


# import os
# print(os.process_cpu_count())
