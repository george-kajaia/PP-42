# class A:
#     def method(self): 
#         print("A")

# class B(A):
#     def method(self): 
#         print("B")

# class C(A):
#     def method(self): 
#         print("C")

# class D(C, B):
#     pass


# d = D()
# print(D.__mro__)
# d.method()


#---abstract method-----------------------------------------------------------------------
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
 
#     def area(self):
#         return 3.14 * self.radius ** 2
 
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# circle = Circle(5)
# print(circle.area()) # 78.5


# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woh")

#     def get_data(self):
#         print("dog's data")

# dog = Dog()
# dog.get_data()
# dog.make_sound()


#---Magic Methods (Dunder Methods)----------------------------------
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return f"{self.name}: ${self.salary}"

#     def __add__(self, other):
#         return self.salary + other.salary

#     def __call__(self):
#         return f"{self.name}: ${self.salary}"
    
#     def __gt__(self, other):
#         if self.salary > other.salary:
#             return True
#         else:
#             return False



# emp1 = Employee("George", 3000)
# print(emp1)
# print(emp1())

# emp2 = Employee("Davit", 4000)
# print(emp1 + emp2)

# if emp1 > emp2:
#     print("True")
# else:
#     print("False")



# class Vector:
#     def __init__(self, x, y):
#         self.x = x; self.y = y
 
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
 
#     def __str__(self):
#         return f"({self.x}, {self.y})"
 
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __mul__(self, scalar):
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x * scalar,self.y * scalar)
#         return NotImplemented

#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return (self.x == other.x and self.y == other.y)
#         return False
 
#     def __bool__(self):
#         return self.x != 0 or self.y != 0
 
#     def __call__(self):
#         return (f"Magnitude: "f"{self.magnitude():.2f}")
 
#     def magnitude(self):
#         return (self.x**2 + self.y**2)**0.

# v = Vector(10, 20)    
# print(v())



class Test:
    def __str__(self):
        return "test string"

    def __call__(self):
        return "test string 2"

test = Test()
print(test)
print(test())
