from config import API_KEY
import requests
from tkinter import Label, PhotoImage, Tk, Button
from PIL import ImageTk, Image
from io import BytesIO
from data import wind_direction
import datetime

PARAM = {"q": "Christchurch",
         "appid": API_KEY,
         "units": "metric"
         }

PARAM2 = {"lon": 172.6333,
          "lat": -43.5333,
          "appid": API_KEY,
          "units": "metric",
          "exclude": "minutely"
          }

RESOURCES = "D35_API-Auth-SMS/resources/"

API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_URL2 = "https://api.openweathermap.org/data/3.0/onecall"

response = requests.get(API_URL, params=PARAM)
response.raise_for_status()

curr_temp = round(float(response.json()["main"]["temp"]), 1)

print(f"currently in {PARAM['q']} is {curr_temp} degrees")

response2 = requests.get(API_URL2, params=PARAM2)
response2.raise_for_status()

# print(response2.json()["hourly"][1]["weather"]["main"])
rain = False
for i in range(12):
    hourly_temp = response2.json()["hourly"][i]["temp"]
    hourly_condition = response2.json()["hourly"][i]["weather"][0]["main"]
    # print(int(response2.json()["hourly"][i]["weather"][0]["id"]))
    # Any weather ID below 700 means some sort of rain
    if int(response2.json()["hourly"][i]["weather"][0]["id"]) < 700:
        rain = True
    print(f"Hourly temp #{i+1}: {hourly_temp}")
    print(f"Hourly conditions #{i+1}: {hourly_condition}")

if rain:
    print("bring an umbrella")
else:
    print("don't bring an umbrella")
# todo create weather app showing current conditions and next 8 hours
# create an UI on tkinter and use this code as base

# UI

window = Tk()
window.config(padx=20, pady=20, bg="black", width=500)
window.title("Christchurch Weather")

current_timestamp = int(response2.json()["current"]["dt"])
converted_datetime = datetime.datetime.fromtimestamp(current_timestamp)
print(f" is currently {converted_datetime}")

current_time_label = Label(text=converted_datetime.strftime("%d/%m %H:%M"),
                           fg="white",
                           bg="black")
current_time_label.grid(row=0)

current_icon = response2.json()["current"]["weather"][0]["icon"]
current_icon_img = Image.open(f"{RESOURCES}{current_icon}@4x.png")
current_icon_img2 = ImageTk.PhotoImage(current_icon_img)
current_label = Label(window, image=current_icon_img2, bg="black")
current_label.grid(row=1)

current_temp = round(float(response2.json()["current"]["temp"]), 1)
current_description = response2.json(
)["current"]["weather"][0]["description"].title()
current_temp_label = Label(
    text=f"{current_description}\n{current_temp}° C",
    font=("arial", 17, ""),
    fg="white",
    bg="black")
current_temp_label.grid(row=2)

current_wind_speed = response2.json()["current"]["wind_speed"]
current_wind_direction = wind_direction(
    float(response2.json()["current"]["wind_deg"]))
current_wind_label = Label(
    text=f"{current_wind_direction} {current_wind_speed} km/h",
    fg="white",
    bg="black"
)
current_wind_label.grid(row=3, pady=20)

window.mainloop()
