def sum_of_digits(n):
    if n < 0:
        raise ValueError("number must be more then 0")
    elif n // 10 == 0:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

print("Sum of numbers is: ", sum_of_digits(11)) 