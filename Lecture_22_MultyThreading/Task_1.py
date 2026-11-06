from multiprocessing import Pool
import sys
import time

def calc_factorial(start_number, end_number):
    result = 1    
    for i in range(start_number, end_number + 1):
        result *= i
    return result


if __name__ == "__main__":
    sys.set_int_max_str_digits(100_000)

    number = 1000
    worker_number = 10

    # ვყოფ რიცხვს ნაწილებად დაახლოებით თანაბრად.
    # ნაწილების რაოდენობას განსაზღვრავს worker_number ცვლადი. 
    # თითოეული ნაწილი შედგება start_number და end_number-სგან და ინახება arguments სიაში.
    # მაგ.: Number = 10, worker_number = 3. arguments = [[1, 4], [5, 8], [9, 10]].
    # ყველა ელემენტში არის თანაბარი რიცხვები გარდა ბოლო ელემენტისა, რომელიც შეიძლება შეიცავდეს ნაკლებ რიცხვს.
    # calc_factorial(start_number, end_number)-ს გადაეცემა ერთი რომელიმე ნაწილი. 
    # მიმდევრობითი დათვლის დროს ციკლში იძახება calc_factorial(start_number, end_number) და 
    # გადაეცემა arguments ერთი ელემენტი. 
    # პარალელური დათვლის დროს კი calc_factorial(start_number, end_number) გადაეცემა სხვადასხვა პროცესს 
    # arguments სიის ერთი ელემენტით.

    chunk_size = number // worker_number
    if number % worker_number != 0:
        chunk_size += 1

    arguments = []
    for i in range(1, worker_number):
        start = chunk_size * (i - 1) + 1
        end = start + chunk_size - 1
        arguments.append([start, end])

    if end != number:    
        arguments.append([end+1, number])
    
# Single-process execution-----------------------------------------------------------------------------
    start_time = time.time()
    result = 1

    for i in range(worker_number):
        result = result * calc_factorial(arguments[i][0], arguments[i][1])

    single_time = time.time() - start_time
    
    print(f"Single-process: Result={result}; time={1000 * single_time:.4f} ms")

# Parallel-process execution---------------------------------------------------------------------------
    start_time = time.time()
    with Pool() as pool:        
        pool_results = pool.starmap(calc_factorial, arguments)      

    result = 1
    for x in pool_results:
        result *= x

    parallel_time = time.time() - start_time
    print(f"Parallel-process: Result={result}; time={1000 * parallel_time:.4f} ms")

    print(f"Single-process time: {1000 * single_time:.4f}x")
    print(f"Parallel-process time: {1000 * parallel_time:.4f}x")

    # ფაქტორიალის დათვლა არც ისე დიდი დატვირთვაა პროცესორისთვის, 
    # ამიტომ პარალელურად დათვალში დამჭირდა უფრო მეტი დრო: parallel_time > single_time. 
    # წავაწყდი ე.წ. multiprocessing overhead-ს