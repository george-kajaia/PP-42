import csv

def read_data():
    with open("titanic.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row


def filter_data():
    func = read_data()

    for row in func:
        if row["Survived"] == '1':
            yield row


def write_data():
    func = filter_data()
    data = next(func)
    header = list(data.keys())

    with open("survived.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header, delimiter = ",")

        writer.writeheader() # Write Header
        writer.writerow(data)  # Write First Row

        for data in func:
            writer.writerow(data) # Write Other Rows


write_data()