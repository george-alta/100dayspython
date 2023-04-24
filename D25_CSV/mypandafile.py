import pandas
data = pandas.read_csv("D25_CSV/weather_data.csv")
# print(type(data))

# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f"average is {round(sum(temp_list) / len(temp_list),2)} ℃")

# print(data["temp"].mean())
# print(data["temp"].max())

# #  get data of a particular row
# print(data[data.day == "Monday"])

# # get value or max temp
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = (monday.temp)
# print(monday_temp)
# monday_temp_f = (monday_temp * 9/5 + 32)

# create a data frame from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("D25_CSV/new_data.csv")
