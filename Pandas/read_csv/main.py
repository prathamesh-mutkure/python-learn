import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temp = []
    data.__next__()

    for row in data:
        temp.append(int(row[1]))

    print(temp)
    print("--------------------------------")

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
