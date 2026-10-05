# def calculate_sum(x, y):
#     print(x + y)

# def print_full_name(first_name, last_name, status = "student"):
#     print(f"{first_name} {last_name}, Status: {status}")


# calculate_sum(3, 5)

# first_name = input("enter the first name: ").capitalize()
# last_name = input("enter the last name: ").capitalize()

# print_full_name(first_name, last_name, "teacher")

# def append_item(item, lst=[]):
#     lst.append(item)
#     print(lst)

# append_item("python")
# append_item("java")


# def append_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     print(lst)

# append_item("python")
# append_item("java", ["1", "2", "3"])

# def full_name(first_name, last_name):
#     return first_name + " " + last_name

# print(full_name("George", "Kajaia"))

# def div_mod(a, b):
#     return a // b, a % b

# print(div_mod(10, 3))


def student(name, age, *args, **dictArgs):
    """
    this is the text function
    """
    return f"{name} is {age} years old, {args} - {dictArgs}"
    
print(student("George", 45, 10, 10, "abcdefgh", height = 10, width=45))