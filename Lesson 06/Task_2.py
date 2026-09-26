inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]
new_items = ["mango", "grape"]

print(f"Apple count:: {inventory.count("apple")}", "\n")
print(f"First index of orange: {inventory.index("orange")}", "\n")

inventory.extend(new_items)
print("Extended list: ", inventory, "\n")
print("List in reverse order: ", inventory[::-1])

