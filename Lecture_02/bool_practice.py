# Read a number from the user. Print
# whether it is positive, negative, or
# zero, and whether it is even or odd.
# Use boolean expressions and
# comparisons.

number = input("enter any integer number: ")
number = int(number)

if number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")

if (number % 2) == 0:
    print("The number is even")
else:
    print("The number is even")
