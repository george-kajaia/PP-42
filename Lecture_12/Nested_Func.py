# def Outer():
#     print("Outer")

#     def Inner():
#         print("Inner")
#         return "Return Inner"

#     # print(Inner())
#     return Inner()

# x = "Global Variable"

# print(Outer())
# print(x)



# # make_counter---------------------------------------------
# def make_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter

# # counter1 = make_counter()
# # print(counter1())
# # print(counter1())
# # print(counter1())

# counter2 = make_counter
# counter3 = counter2()
# print(counter3())
# print(counter3())
# print(counter3())



# # make_multiplier-----------------------------------------
# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor  # 'factor' is remembered
#     return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))  # 10
# print(triple(5))  # 15


# #decorator-----------------------------------------
# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello() 

# hello = my_decorator(say_hello)
# hello()



# #---Time decorator-----------------------------------------
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"Function took {(end - start)*1000000} mikroseconds to execute.")
#     return wrapper

# @timer
# def calculator(a, b):
#     time.sleep(2)
#     print(a ** b)

# calculator(2, 3) 

# #---Logger decorator-----------------------------------------
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} is called with arguments: {args} and keyword arguments: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned: {result}")
#         return result
    
#     return wrapper

# @log_decorator
# def calculate(a, b, operation):
#     return a ** b

# a = calculate(2, b = 3, operation = "power")
# print(a)

# #---Decorator with parameters-----------------------------------------
# def repeat_decorator(times=5):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat_decorator(2)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("John")  # This will print "Hello, John!" three times



# #-- Decorator with parameters and metadata preservation
# from functools import wraps

# def repeat_decorator(times=5):
#     def decorator(func):
#         @wraps(func)  # This preserves the original function's metadata
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat_decorator(2)
# def greet(name):
#     """Greets a person by name."""
#     print(f"Hello, {name}!")    

# greet("John")  # This will print "Hello, John!" two times



#-- Test 
import time
from functools import wraps

def timer(perfomance_time=2.0):
    def decorator(func):
        @wraps(func)    
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > perfomance_time:
                print("Function too long")            
            return result        
        return wrapper    
    return decorator

@timer(2)
def calculator(a, b, operation):
    """Conducts an operations on a and b"""
    time.sleep(3)
    print("Calculating {a} {operation} {b}")
    return a ** b

print(calculator(2, 3, operation = "power"))

