# import Module_two
# sum = Module_two.add(2, 3)

# from Module_two import add 
# sum = add(2, 3)

# print(sum)


# from .Module_two import add
# sum = add(2, 3)
# print(sum)

# from . import divide
# sum = divide(10, 2)
# print(sum)

# -------------------------------------------

# import faker

# fake = faker.Faker()
# print(fake.first_name())
# print(fake.last_name(),)
# print(fake.email())
# print(fake.address())

# -------------------------------------------

from faker import Faker 

fake = Faker()
print(fake.first_name())
print(fake.last_name(),)
print(fake.email())
print(fake.address())
