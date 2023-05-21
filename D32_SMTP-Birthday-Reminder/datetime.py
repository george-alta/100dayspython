import datetime as dt
now = dt.datetime.now()  # current day and time
year = now.year
day_of_week = now.weekday()


if year == 2023:
    print("happy 2023")
print(day_of_week)

day_of_birth = dt.datetime(year=1980, month=1, day=10, hour=5)
print(day_of_birth)
