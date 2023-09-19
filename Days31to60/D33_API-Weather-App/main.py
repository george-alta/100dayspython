import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # this returns the 200 code: OK

response.raise_for_status()

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

print(f"latitude {latitude}, longitude {longitude}")

iss_position = (latitude, longitude)
print(iss_position)
