class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


manager = Manager("George", 1500, "head_office") 
manager.get_info()