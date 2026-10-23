class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self._bank = bank
        self.__balance = balance

    # def get_balance(self):
    #     return self.__balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        self.__balance = value

    @balance.deleter
    def balance(self):
        del self.__balance


acc = BankAccount("John", "Step", 1000)
print(acc.name)

acc.name = "Ana"
print(acc.name)

print(acc._bank)
acc._bank = "Tbilisi"
print(acc._bank)

print(acc.__balance)
acc.__balance = 2000
print(acc.__balance)

# print(acc.get_balance())

print(acc.balance)

acc.balance = 5000
print(acc.balance)

del acc.balance
print(acc.balance)



class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def bark(self):
        print(f"{self.name} is barking")


class GoldenRetriever(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def play(self):
        print(f"{self.name} is playing")


class Cat(Animal):
    def __init__(self, name, age, eye_color):
        super().__init__(name, age)
        self.eye_color = eye_color

    def meow(self):
        print(f"{self.name} is meowing")


dog_1 = Dog("Bob", 2, "Black")
print(dog_1)
dog_1.eat()
dog_1.sleep()
dog_1.bark()
print(dog_1.color)

cat_1 = Cat("Tom", 1, "Brown")
print(cat_1)
cat_1.eat()
cat_1.sleep()
cat_1.meow()
print(cat_1.eye_color)

gr_1 = GoldenRetriever("Bob", 2, "Black")
print(gr_1)
gr_1.eat()
gr_1.sleep()
gr_1.bark()
gr_1.play()
print(gr_1.color)



class Shape:
    def area(self):
        raise NotImplementedError("Area method is not implemented")
    
class Circle(Shape):
    color = "Red"

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    @classmethod
    def circle_color(cls):
        return cls.color
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    @staticmethod
    def pi():
        return 3.14
    

circle_1 = Circle(10)
print(circle_1.area())
print(circle_1.circle_color())

# rec_1 = Rectangle(10, 20)
# print(rec_1.area())

print(Rectangle.pi())