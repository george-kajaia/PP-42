class Student:
    university = "IT Academy Step"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        self.gpa = 0
        self.year = 1

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)       
        else:
            print(f"{course} is already added")

    def display(self):
        print(f"University: {self.university}")
        print(f"Courses: {self.courses}")
        print(f"GPA: {self.gpa}")
        print(f"Year: {self.year}")


print("=" * 40)
student1 = Student("John", 20)
student1.add_course("Python")
student1.add_course("Java")
student1.add_course("Java")
student1.display()
print(student1.name)
print(student1.age)
print(student1.university)