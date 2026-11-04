import multiprocessing
import time
import math

def calc_factorial(number1, number2):
    for i in range(number1, number2 + 1):
        result *= i

    return result


number = 100_000
start_time = time.time()
result = calc_factorial(1, number)
single_time = time.time() - start_time
print(f"Single-process time: {single_time:.4f} seconds")

workers = 10

chunk_size = number // workers



    ranges = [
        (start, min(start + chunk_size - 1, n))
        for start in range(1, n + 1, chunk_size)
    ]

    # 1. Single-process
    start_time = time.time()

    parts = [factorial_part(r) for r in ranges]
    result_single = math.prod(parts)

    single_time = time.time() - start_time

    # 2. Multiprocessing
    start_time = time.time()

    with multiprocessing.Pool(processes=workers) as pool:
        parts = pool.map(factorial_part, ranges)

    result_multi = math.prod(parts)

    multi_time = time.time() - start_time

    # Compare results
    print(f"Single-process time: {single_time:.4f} seconds")
    print(f"Multiprocessing time: {multi_time:.4f} seconds")
    print(f"Results equal: {result_single == result_multi}")
    print(f"Speedup: {single_time / multi_time:.2f}x")