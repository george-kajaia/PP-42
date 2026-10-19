import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# people = [
#     ["George", "Kajaia"],
#     ["Tamuna", "Rapava"],
#     ]

# with open("test.csv", "w", newline="") as file:
#     write = csv.writer(file)   
#     write.writerow(["Name", "Age"])    
#     write.writerows(people)


# with open("test.csv", "r") as file:
#     reader = csv.DictReader(file)   
#     for row in reader:
#          print(row)

headers = ["id", "name"]
people = [ 
    {"id": 1, "name": "george"},
    {"id": 2, "name": "tamuna"}
]

# with open("test_dict.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=headers, delimiter = ";")

#     writer.writeheader()
#     writer.writerows(people)

with open("test_dict.csv", "r") as file:
    reader = csv.DictReader(file, delimiter = ";")
    
    print(reader.fieldnames)

    for row in reader:         
        print(row)        
        print(row["id"], row["name"])
