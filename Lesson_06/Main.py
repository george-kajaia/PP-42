# empty_list = []

# empty_list = list()

# print(empty_list)

# print(type(empty_list))

# numbers: list[int] = [1, 2, 3, 4 ,5]

# print(numbers)

# mixed: any = [1, 'Nino Aptsiauri', False, 3.14]

# mixed = [1, 'Nino Aptsiauri', False, 3.14]

# print(mixed)


# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist.insert(1000, "orange")
# print(thislist)

# thislist.remove("cherry")
# print(thislist)

# thislist.pop(1)
# print(thislist)

# print("-----------------")

# thislist.pop()
# print(thislist)

# thislist.pop()
# print(thislist)

# thislist.append(1)
# print(thislist)
# thislist.pop()
# print(thislist)

# thislist.insert(100, False)
# print(thislist)
# thislist.pop()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# for c in thislist: 
#     print(c)

# print("-------------------------------------------------")

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# for i in range(len(thislist)): 
#     print(thislist[i])


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for c in fruits:
#     if "a" in c:
#         newlist.insert(-1, c)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# newlist = [c for c in fruits if "a" in c]

# print(newlist)


# thislist = [10, 25, 12, 17, 9]
# thislist.sort()
# print(thislist)

# thislist.sort(reverse=True)
# print(thislist)

# first_list = [10, 25, 12, 17, 9]
# print(first_list)

# second_list = first_list
# print(second_list)

# first_list[0] = 100

# print(first_list)
# print(second_list)

# third_list = first_list.copy()
# forth_list = list(first_list)
# print("-------------------------------------")
# first_list[0] = 999
# print(first_list)
# print(second_list)
# print(third_list)
# print(forth_list)


# first_list = [10, 15, 22, 27, 29]

# print(first_list)
# second_list = first_list[:3]
# first_list[0] = 100
# print(second_list)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1.extend(list2)
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# list3 = list1
# print(list3)


# list1 = ["a", "b", "c"]
# list1.clear()
# print(list1)

# print(list1)
# print(list1.count("a"))

# fruits = ['apple', 'banana', 'cherry', True, False, 152, 'cherry']
# print(id(fruits))
# print(fruits.index("cherry"))


# fruits.reverse()
# print(fruits)
# print(fruits.__len__())


# fruits = [1, 1, 1]
# print(sum(fruits))
# print(id(fruits))

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)
# mytuple2 = "apple", "banana", "cherry"
# print(mytuple2)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# x = ("apple", "banana", "cherry")
# print(x)
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)