# scores: list[int] = [56, 67, 90, 38, 40, 79]
# passed_scores: list[int] = [i if i>=60 else f"{i}" for i in scores]
# print(passed_scores)

# tup = ("Tbilisi", "Tbilisi")
# tup[1] = "abc"
# print(tup[1])
# print(tup)


# student = {
#     "name": "ana",
#     1: "sss"
# }
# print(student)


# empty_dct: dict[any, any] = {}
# print(empty_dct)
# empty_dct2 = dict()
# print(empty_dct2)
# empty_dct3 = {}
# print(empty_dct3)

# scores: dict[str, int] = {
#     "python": 90,
#     "JAVA": 92
#     }
#print(scores)

# scores2 = dict(python=90, JAVA = 92, JavaScript = 95)
# print(scores2)

#-------------------------------------------------------------

# scores.clear();
# print(scores)

# del scores["JAVA"]
# print(scores)

# del scores
# print(scores)

# str = scores.pop("JAVA")
# print(scores)
# print(str)


# str = scores.pop("C++", None)
# print(scores)
# print(str)

# removed_items = scores.popitem()
# print(scores)
# print(removed_items)
# print(type(removed_items))

# language, value = removed_items
# print(language, value)

# print(scores.keys())
# print(scores.values())
# print(scores.items())
# print(len(scores))

# for key, value in scores.items():    
#     print(f"Key={key}, value={value}")

# dict: dict[any, any] = {i: i**2 for i in range(1, 6) if i %2 ==0 }
# print(dict)

# person = {
#     "name": "Anna",
#     "age": 20,
#     "scores": {
#         "Python": 97,
#         "Java": 90
#     }  
# }

# print(person)

# score = person["scores"]
# print(score)
# python_score = score["Python"]
# print(python_score)
# print(person["scores"]["Java"])


# languages = {"Python", "Java", "Python", "C++"}
# print(languages)

# lst = [1, 1, 2, 2, 3, 3, 4, 4]
# unique_numbers = list(set(lst))
# print(unique_numbers)

set1 = {1, 2, 3, 4, 5}
set2 = {      3, 4, 5, 6, 7}

# set0 = set1 | set2
# print(set0)
# print(set1.union(set2))

# set0 = set1 & set2
# print(set0)
# print(set1.intersection(set2))

# set0 = set1 - set2
# print(set0)
# print(set1.difference(set2))

# set0 = set1 ^ set2
# print(set0)
# print(set1.symmetric_difference(set2))

set1.difference_update(set2)
print(set1)