import pandas
data = pandas.read_csv(
    "D25_CSV/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# "Primary Fur Color"
# count

data_frame = data.groupby(['Primary Fur Color'])['Primary Fur Color'].count()
print(data_frame)
data_frame.rename(index={0: "Fur Color", 1: "Count"})
print(data_frame)
data_frame.to_csv("D25_CSV/squirrel/squirrels_by_color.csv")
