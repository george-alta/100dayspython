import datetime


time = 1685381909

converted_datetime = datetime.datetime.fromtimestamp(time)

print(converted_datetime)
offset = datetime.timedelta(seconds=43200)

current_time = converted_datetime + offset
print(current_time)
