# A simple Tkinter window showing:
# 1: the sunrise and sunset times for AKL timezone (UTC+12)
# 2: Current weather conditions at Christchurch


import requests
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta
from tkinter import Tk, PhotoImage, Label, Canvas
from weathercodes import weathercodes

MY_LAT = -43.53
MY_LON = 172.63


def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert coordinates from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Radius of the Earth in kilometers
    earth_radius = 6371.0

    # Calculate the differences between the coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Apply the Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = round(earth_radius * c)

    return distance


# get ISS position
iss_pos = requests.get("http://api.open-notify.org/iss-now.json")
# iss_result = iss_pos.json()
iss_lat = float(iss_pos.json()["iss_position"]["latitude"])
iss_lon = float(iss_pos.json()["iss_position"]["longitude"])
print(f"lat{iss_lat}, long{iss_lon}")

# AKL: UTC + 12 hours
response = requests.get(
    "http://api.sunrise-sunset.org/json?lat=-43.532055&lng=172.636230")
# jsonresult = response.json()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]

# str format for the API response
time_format = "%I:%M:%S %p"
# UTC + 12
offset = timedelta(hours=12)
# convert string to datetime object
datetime_sunrise = datetime.strptime(sunrise, time_format)+offset
datetime_sunset = datetime.strptime(sunset, time_format)+offset

# current weather conditions API
curr_weather = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=-43.53&longitude=172.63&current_weather=true")
jsonresult2 = curr_weather.json()
curr_temperature = curr_weather.json()["current_weather"]["temperature"]
curr_wind = curr_weather.json()["current_weather"]["windspeed"]
curr_conditions = curr_weather.json()["current_weather"]["weathercode"]
curr_time = curr_weather.json()["current_weather"]["time"]
datetime_current = datetime.strptime(curr_time, "%Y-%m-%dT%H:%M") + offset
print(weathercodes[curr_conditions])
curr_time_str = datetime_current.strftime("%H:%M")

# create UI
window = Tk()
window.title("My weather app")
window.config(padx=50, pady=50)

# top images
sunset_img = PhotoImage(file="D33_API/resources/sunset.png")
sunrise_img = PhotoImage(file="D33_API/resources/sunrise.png")
canvas = Canvas(width=1024, height=410, highlightthickness=0)
canvas.create_image(256, 200, image=sunrise_img)
canvas.create_image(256+512, 200, image=sunset_img)
canvas.grid(column=0, row=0, columnspan=2)

# labels sunrise and sunset
sunrise_label = Label(text=datetime_sunrise.strftime(
    "%H:%M:%S"), font=("arial", 30, "bold"))
sunrise_label.grid(column=0, row=1)
sunset_label = Label(text=datetime_sunset.strftime(
    "%H:%M:%S"), font=("arial", 30, "bold"))
sunset_label.grid(column=1, row=1)

# current conditions labels
now_label = Label(
    text=f"\n\nCurrently in Chistchurch: {curr_temperature} C, Wind: {curr_wind} km/h", font=("arial", 22, "bold"))
now_label.grid(column=0, row=2, columnspan=2)
current_conds_label = Label(
    text=f"{weathercodes[curr_conditions]}\n\nUpdated: {curr_time_str}", font=("arial", 17, "italic"))
current_conds_label.grid(column=0, row=3, columnspan=2)

iss_label = Label(
    text=f"Current ISS coordenates. Lat: {iss_lat} Lon: {iss_lon} The ISS is now {calculate_distance(iss_lat, iss_lon, MY_LAT, MY_LON)} KMS away!")
iss_label.grid(column=0, row=4, columnspan=2)

# customise label if ISS is close enough and is nightime
if int(curr_weather.json()["current_weather"]["is_day"]) == 0 and calculate_distance(iss_lat, iss_lon, MY_LAT, MY_LON) < 10000:
    look_up_label = Label(text="Look up, you may find the ISS up in the sky")
    look_up_label.grid(column=0, row=5, columnspan=2)
    # the original challenge was a terminal app with an email triggered notification,
    # but this label covers the same functionality
    # also the original challenge required a while loop running every 60 seconds
    # using time.sleep(60)


window.mainloop()


# Example coordinates
lat1 = 40.7128  # Latitude of point 1 (New York City)
lon1 = -74.0060  # Longitude of point 1 (New York City)
lat2 = 34.0522  # Latitude of point 2 (Los Angeles)
lon2 = -118.2437  # Longitude of point 2 (Los Angeles)

# Calculate the distance between the coordinates
distance = calculate_distance(lat1, lon1, lat2, lon2)
print(distance)
