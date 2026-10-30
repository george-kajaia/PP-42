# class BankAccount:
#     def __init__(self, name, bank, balance):
#         self.name = name
#         self._bank = bank
#         self.__balance = balance

#     # def get_balance(self):
#     #     return self.__balance

#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, value):
#         self.__balance = value

#     @balance.deleter
#     def balance(self):
#         del self.__balance


# acc = BankAccount("John", "Step", 1000)
# print(acc.name)

# acc.name = "Ana"
# print(acc.name)

# print(acc._bank)
# acc._bank = "Tbilisi"
# print(acc._bank)

# print(acc.__balance)
# acc.__balance = 2000
# print(acc.__balance)

# # print(acc.get_balance())

# print(acc.balance)

# acc.balance = 5000
# print(acc.balance)

# del acc.balance
# print(acc.balance)



# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"


# class Dog(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def bark(self):
#         print(f"{self.name} is barking")


# class GoldenRetriever(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age, color)

#     def play(self):
#         print(f"{self.name} is playing")


# class Cat(Animal):
#     def __init__(self, name, age, eye_color):
#         super().__init__(name, age)
#         self.eye_color = eye_color

#     def meow(self):
#         print(f"{self.name} is meowing")


# dog_1 = Dog("Bob", 2, "Black")
# print(dog_1)
# dog_1.eat()
# dog_1.sleep()
# dog_1.bark()
# print(dog_1.color)

# cat_1 = Cat("Tom", 1, "Brown")
# print(cat_1)
# cat_1.eat()
# cat_1.sleep()
# cat_1.meow()
# print(cat_1.eye_color)

# gr_1 = GoldenRetriever("Bob", 2, "Black")
# print(gr_1)
# gr_1.eat()
# gr_1.sleep()
# gr_1.bark()
# gr_1.play()
# print(gr_1.color)



# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method is not implemented")
    
# class Circle(Shape):
#     color = "Red"

#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     @classmethod
#     def circle_color(cls):
#         return cls.color
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     @staticmethod
#     def pi():
#         return 3.14
    

# circle_1 = Circle(10)
# print(circle_1.area())
# print(circle_1.circle_color())

# # rec_1 = Rectangle(10, 20)
# # print(rec_1.area())

# print(Rectangle.pi())



#---Class Methods------------------------------------------------

# class Date:
#     def __init__(self, day, month, year):
#         self.day, self.month, self.year = day, month, year
    
#     @classmethod
#     def from_string(cls, date_string):
#         """Create a Date from a 'DD-MM-YYYY' string."""
#         day, month, year = map(int, date_string.split("-"))
#         return cls(day, month, year) # Calls __init__
 
#     @classmethod
#     def today(cls):
#         """Create a Date for today's date."""
#         import datetime
#         t = datetime.date.today()
#         return cls(t.day, t.month, t.year)
    
#     def __str__(self):
#         return f"{self.day:02d}/{self.month:02d}/{self.year}"
    
# d1 = Date(15, 9, 2024) # Normal constructor
# d2 = Date.from_string("25-12-2024") # Class method
# d3 = Date.today() # Class method

# print(d1)
# print(d2)
# print(d3)


class Employee:
    company = "Microsoft"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_company(cls):
        return cls.company
    
print(Employee.get_company())  # Microsoft

emp = Employee("George")
print(emp.get_company())
print(Employee.get_company())



#---Static Methods------------------------------------------------

# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def is_even(n):
#         return n % 2 == 0

#     @staticmethod
#     def factorial(n):
#         if n == 0:
#             return 1
#         return n * MathUtils.factorial(n - 1)
    
#     @staticmethod
#     def clamp(value, min_val, max_val):
#         return max(min_val, min(value, max_val))
    
# # No object needed — call on the class directly
# print(MathUtils.add(3, 7)) # 10
# print(MathUtils.is_even(4)) # True
# print(MathUtils.factorial(5)) # 120
# print(MathUtils.clamp(150,0,100)) # 100

# mt = MathUtils()
# print(mt.add(3, 7))