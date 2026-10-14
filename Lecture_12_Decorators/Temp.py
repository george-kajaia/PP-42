
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_execution
def calculate_sum(a, b):
    """Returns the sum of two numbers."""
    return a + b


print(calculate_sum(10, 20))
print(calculate_sum.__name__)
print(calculate_sum.__doc__)
