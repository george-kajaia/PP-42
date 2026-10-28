class PhoneBook:
    user_phones = dict()

    @staticmethod
    def get_phone_by_name(name):
        return PhoneBook.user_phones.get(name, "unknown")

    @staticmethod
    def add_phone(name, phone):
        PhoneBook.user_phones[name] = phone
        print(f"A new phone number was added. name: {name};   phone: {phone} ")


PhoneBook.add_phone("გიორგი", "555000000")
PhoneBook.add_phone("ანა", "555111111")
PhoneBook.add_phone("ნიკა", "555222222")
PhoneBook.add_phone("მარიამი", "555333333")

print("\n")

name = "გიორგი"
print(f"{name}'s phone number is: {PhoneBook.get_phone_by_name(name)}")

name = "ანა"
print(f"{name}'s phone number is: {PhoneBook.get_phone_by_name(name)}")

name = "ნიკა"
print(f"{name}'s phone number is: {PhoneBook.get_phone_by_name(name)}")

name = "მარიამი"
print(f"{name}'s phone number is: {PhoneBook.get_phone_by_name(name)}")

name = "ჯუმბერი"
print(f"{name}'s phone number is: {PhoneBook.get_phone_by_name(name)}")
