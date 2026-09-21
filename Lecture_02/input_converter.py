# Ask the user for their birth year
# using input(). Cast it to int,
# subtract from 2025, and print their
# approximate age.

age = input("enter your birth year: ")
age = int(age)
print("user is " + str(2026 - age) + " years old")
