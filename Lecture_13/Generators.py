# test_list = [10, 2, 6, 5, 8, 9]

# iter_list = iter(test_list)
# print(type(iter_list)) # <class 'list_iterator'>

# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))




# def generator_func(num):
#     while True:
#         if num == 0:
#             break
#         yield num
#         num -= 1
#     print("Done counting down!")

# func = generator_func(30)

# print(next(func))
# print(next(func))
# print(next(func))

# for i in func:
#     print(i)


# def odd_nums():
#     num = 1
#     while True:
#         yield num
#         num += 2

# func = odd_nums()

# print(next(func))
# print(next(func))
# print(next(func))
# print(next(func))



#  generator expression
squares_list = [x * x for x in range(1000)] #list comprehension

squares_gen = (x * x for x in range(1000)) # generator expression

# print(squares_list)
# print(next(squares_gen), "\n")

# for i in squares_gen:
#     print(i)



# import sys
# list_method = sys.getsizeof(squares_list)
# gen_method = sys.getsizeof(squares_gen)

# print(list_method)
# print(gen_method)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))



# def acumulator():
#     total = 0
#     while True:
#         value = yield total
#         if value is None:
#             break

#         total += value


# acc = acumulator()

# #print(acc.send(None))  # Initialize the generator
# print(next(acc))  # Output: 0
# print(acc.send(10))
# print(acc.send(20))



def generator_1():
    yield "A"
    yield "B"

def generator_2():
    yield "C"
    yield "D"

def combined_generator():
    yield from generator_1()
    yield from generator_2()

    # for value in generator_1():
    #     yield value
    # for value in generator_2():
    #     yield value

func = combined_generator()

for i in func:
    print(i)


iter_gen_list = iter(combined_generator())
#print(type(iter_gen_list)) # <class 'generator'>

for i in iter_gen_list:
    print(i)

# print(next(iter_gen_list))
