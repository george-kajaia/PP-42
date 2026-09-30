# try:
#     number1 = int(input("Enter the number1: "))
#     number2 = int(input("Enter the number2: "))
#     result = number1 / number2
#     print(result)
# except:
#     print("Something went wrong")

# try:
#     for i in range(10000000000000):
#         print(i)
# except:
#     print("Something went wrong")

# for i in range(10000000000000):
#     print("after exception")


try:
#    open("abcde.txt")
    number1 = int(input("Enter the number1: "))    
    number2 = int(input("Enter the number2: "))
    result = number1 / number2
    print(result)
except ValueError:
    print("Value must be int")
except ZeroDivisionError:
    print("Value must be more then zero")
except Exception as e:
    print(f"Something went wrong: {e}")
