# import multiprocessing
# def cpu_task(n):
#     return sum(i * i for i in range(n))

# if __name__ == "__main__":
#     processes = [ multiprocessing.Process(target=cpu_task, args=(10_000_000,) ) for _ in range(4)]
#     for p in processes: p.start()
#     for p in processes: p.join()



from multiprocessing import Pool

def cpu_task(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    inputs = [10_000_000] * 8
    with Pool() as pool:
        results = pool.map(cpu_task, inputs)

    print(results)
 # Pool sizes to number of CPU cores
 # pool.map() blocks until all don