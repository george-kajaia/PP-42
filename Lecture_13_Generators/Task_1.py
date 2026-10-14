def even_numbers():
    num = 2
    while True:
        yield num
        num += 2

func = even_numbers()

for i in range(10):
    print(next(func))