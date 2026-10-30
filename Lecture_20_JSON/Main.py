# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name: str
#     salary: float = 1000

# emp = Employee("giorgi, 333")

# for x in emp.__dict__:
#     print(x)

# print("\n")

# for x in Employee.__dict__:
#     print(x)

# print(Employee.salary)

import json

data = {"name": "Alice", "age": 30}

text = json.dumps(data)
print(text) 

print("\n")

ext = '{"name": "Alice", "age": 30}'
data = json.loads(text)
print(data["name"]) 