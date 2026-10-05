def create_user_profile(first_name, last_name, role="Student", is_active=True):
     student = {
        "first_name": first_name,
        "last_name": last_name,
        "role": role, 
        "is_active": is_active
     }

     return student

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

print(create_user_profile(first_name, last_name))