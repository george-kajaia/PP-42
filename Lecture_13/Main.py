import time
from functools import wraps

def log_execution(func):

    def wrapper():
        print(f"Running the '{func.__name__}' function with arguments: {args} ")        
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Executed in {(end_time - start_time)*1000000} microseconds")
        
        return result
    
    return wrapper

@log_execution
def calculate(a, b):
    """calculating  a in the b-th power"""
    return a ** b

a = calculate(2, 3)
print(f"Result of calculation: {a}")