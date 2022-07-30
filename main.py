FILENAME = "msg.txt"
msgs = []

for i in range(4):
    msg = input("Введите строку {i}: ")
    msgs.append(msg + "\n")

with open(FILENAME, 'a') as file:
    for msg in msgs:
        file.write(msg)

with open(FILENAME) as file:
    for msg in file:
        print(msg, end="")


import csv

FILENAME = 'users.csv'
users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FILENAME, 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, 'a', newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, 'r', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} - {row[1]}")