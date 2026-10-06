
# lst = [1, 8, 5, 2, 3, 9, 4, 7, 6]

# sorted_lst = sorted(lst)
# print(sorted_lst)

# sorted_lst = sorted(lst, reverse=True)
# print(sorted_lst)



# students = [
#     ("John", 85),
#     ("Anna", 90),
#     ("Bob", 75),
#     ("Alice", 92)
# ]

# sorted_students = sorted(students, key=lambda student: student[1])
# print(sorted_students)


# def get_score(student):
#     return student[1]

# sorted_students = sorted(students, key=get_score, reverse=True)
# print(sorted_students)



# people = [
#     ("John", 20, 85),
#     ("Anna", 21, 90),
#     ("Bob", 20, 75),
#     ("Alice", 21, 92)
# ]

# sorted_people = sorted(people, key=lambda person: (person[1], person[2]), reverse=True)
# print(sorted_people)



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mapped_nums = list(map(lambda x: x * 2, nums))
# print(mapped_nums)

# mapped_nums = list(map(lambda num: num * 2 if num % 2 == 0 else num, nums))
# print(mapped_nums)

# def map_func(N):
#     if N % 2 == 0:
#         return N * 2
#     else:
#         return N

# mapped_nums = list(map(map_func, nums))
# print(mapped_nums)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_nums = list(filter(lambda num: num % 2 == 0, nums))
# print(filtered_nums)

# def filter_func(x):
#     return x % 2 == 0

# filtered_nums = list(filter(filter_func, nums))
# print(filtered_nums)



from functools import reduce

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# sum_of_nums = reduce(lambda acc, num: acc + num, lst)
# print(sum_of_nums)

# def add(acc, num):
#     return acc + num

# lst = ["1", "2", "3", "4", "a"]

# sum_of_nums = reduce(add, lst)

# print(sum_of_nums)


student_names = ["John", "Anna", "Bob"]
student_scores = [85, 90, 75, 77, 91]

student_info = list(zip(student_names, student_scores))
print(student_info)


student_names = ["John", "Anna", "Bob", "Alice"]
student_scores = [85, 90, 75, 77, 91]
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi"]

student_infos = list(zip(student_names, student_scores, cities))
print(student_infos)