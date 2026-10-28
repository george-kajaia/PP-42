class Salary:
    def __get__(self, instance, owner):
        print("Getting salary")
        return instance._salary1

    def __set__(self, instance, value):
        print("Setting salary")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        instance._salary1 = value


class Employee:
    salary = Salary()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# emp = Employee("George", 3000)
# print(emp.salary)  # 3000
# emp.salary = 5000
# print(emp.salary)  # 5000

# emp2 = Employee("Nino", 111)
# print(emp2.salary)
# emp2.salary = 222
# print(emp2.salary)  # 5000

# emp = Employee("Davit", 3000)

# print(Employee.__dict__["salary"])

# for x in emp.__dict__:
#     print(x)

# print("-------------")

# for x in Salary.__dict__:
#     print(x)


emp = Employee("George", 3500)
emp2 = Employee("George", 777)

for x in emp.__dict__:
     print(x)

emp.__dict__["salary"] = 9000

print(emp.__dict__)
print(emp.salary)
print(emp2.salary)