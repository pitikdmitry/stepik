import csv
from datetime import datetime

crimes = dict()

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    row_1 = next(reader)
    date_num = 2
    type_num = 5

    for row in reader:
        if "2015" in row[date_num]:
            type = row[type_num]
            if type in crimes:
                crimes[type] = crimes[type] + 1
            else:
                crimes[type] = 1

max = 0
type = ""
for key, val in crimes.items():
    # print(val)
    if val > max:
        max = val
        type = key

print(type)
