import csv

def read_data():
    with open("ssl_companies.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row


def filter_data():
    func = read_data()

    for row in func:
        if int(row["Number of employees"]) > 1000:
            yield row


def write_data():
    func = filter_data()
    data = next(func)
    header = ["Name", "Industry", "Number of employees"]

    with open("sorted_companies.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header, delimiter = ",", extrasaction="ignore")

        writer.writeheader() # Write Header
        writer.writerow(data) # Write Other Rows

        for data in func:
            writer.writerow(data) # Write Other Rows


write_data()