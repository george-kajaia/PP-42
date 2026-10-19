import csv

def read_data():
    with open("titanic.csv", "r") as file:
        reader = csv.reader(file)

        return list(csv.reader(file))

def filter_data(data):
    survived = []

    survived.append(data[0])

    for i in range(1, len(data) - 1):
        if data[i][1] == '1':
            survived.append(data[i])
    return survived

def write_data(data):
    with open("ZZZ_survived.csv", "w", newline="") as file:
        write = csv.writer(file)   
        write.writerows(data)

data = read_data()
data = filter_data(data)
write_data(data)