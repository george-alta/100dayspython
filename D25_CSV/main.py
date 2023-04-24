
# with open("D25_CSV\weather_data.csv") as file:
#     data = file.readlines(55)
#     print(data)

import csv

with open("D25_CSV\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
