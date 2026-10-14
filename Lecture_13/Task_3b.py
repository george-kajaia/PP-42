import sys

def greeter_bot():
    while True:        
        name = yield "What is your name?"
        if name is None:
            print("No name provided.")
            sys.exit(0)
        else:
            print(f"Hello, {name}")

func = greeter_bot()

print(next(func))
print(func.send("George"))
print(func.send("Daviti"))
print(func.send("Irakli"))
print(func.send("Nino"))
print(func.send("Mariami"))
print(next(func))