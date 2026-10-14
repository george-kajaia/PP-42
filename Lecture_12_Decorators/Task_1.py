# #---version 1---
# def make_counter(start_value = 0):
#     count = start_value

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter

#---version 2---
def make_counter(start_value = 0):

    def counter():
        nonlocal start_value
        start_value += 1
        return start_value

    return counter

counter1 = make_counter(5)

print(counter1())  # Output: 6
print(counter1())  # Output: 7
print(counter1())  # Output: 8
