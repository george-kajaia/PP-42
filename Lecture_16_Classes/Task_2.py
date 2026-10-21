class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print(f"User name: {self.username}")
        print(f"User email: {self.email}")
        print(f"User age: {self.age}", "\n")


user1 = User("George", "george_kajaia@yahoo.com", 45)
user2 = User("Daviti", "davit_davitadze@yahoo.com", 45)


user1.get_info()
user2.get_info()

print(f"User1 status: {user1.status}")
print(f"User2 status: {user2.status}")