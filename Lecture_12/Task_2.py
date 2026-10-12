import time

#---Logger decorator---
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}', {func.__doc__}, is called with arguments: {args} and keyword arguments: {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' returned: {result}")
        print(f"Running '{func.__name__}' Executed in {(end_time - start_time)*1000000} microseconds")

        return result
    
    return wrapper

@log_execution
def calculate(a, b, operation):
    """calculating the operation on a and b"""
    return a ** b

a = calculate(2, 3, operation = "power")
print(a)
