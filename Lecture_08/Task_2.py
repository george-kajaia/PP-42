person = {
    "name": "Anna",
    "contacts": {
        "mail":"ana@gmail.com",
        "phone":"598 438 298",
        "address": "Georgoa, Tbilisi, nutsubidze plato III",        
    },
    "courses": {
        "Python": {
            "Score": 90,
            "Passed": True
        },
        "Java": {
            "Score": 80,
            "Passed": True
        },
        "Web" : {
            "Score": 50,
            "Passed": False
        },
    }  
}

print("Person: ", person, "\n")

print("Ann's mail: ", person["contacts"]["mail"], "\n")
print("Ann's Python's score: ", person["courses"]["Python"]["Score"], "\n")


person["courses"]["Web"]["Score"] = 65
person["courses"]["Web"]["Passed"] = True

print("Ann's Web's new score", person["courses"]["Web"]["Score"], "\n")
print("Ann's Web course is passed: ", person["courses"]["Web"]["Passed"], "\n")

person["contacts"].pop("phone", None)
print("Ann's contacts: ", person["contacts"])