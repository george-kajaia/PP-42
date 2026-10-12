import time
from functools import wraps

def log_execution(func):

    @wraps(func)
    def wrapper(*args):

        print(f"Running the '{func.__name__}' function with arguments: {args} ")        
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"Executed in {(end_time - start_time)*1000000:.2f} microseconds")
        
        return result
    
    return wrapper

@log_execution
def calculate(a, b):
    """calculating  a in the b-th power"""
    return a ** b

a = calculate(2, 3)

print(f"Result of calculation: {a}")
print(f"function name is: {calculate.__name__}")
print(f"function docstring is: {calculate.__doc__}")
