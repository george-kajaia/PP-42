def greeter_bot():
    while True:        
        name = yield "What is your name?"
        print(f"Hello, {name}")

func = greeter_bot()

print(next(func))
print(func.send("George"))
print(func.send("Daviti"))
print(func.send("Irakli"))
print(func.send("Nino"))
print(func.send("Mariami"))