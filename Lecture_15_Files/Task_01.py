def write_quote():
    writer = input("Enter your favorite writer's name: ")
    quote = input("Enter your favorite writer's quote: ")

    data = f"{writer}: '{quote}'"

    with open("quotes.txt", "w") as file:
        file.write(data)

def read_quote():
    with open("quotes.txt", "r") as file:
        data = file.read()
    
    print(data)

write_quote()
read_quote()