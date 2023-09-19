from config import TEQUILA_API_KEY, FLIGHT_SEARCH
import requests

SERVER = "https://api.tequila.kiwi.com/v2/search"

HEADERS = {"accept": "application/json", "apikey": TEQUILA_API_KEY}

params = {"fly_from": "AKL",
          "fly_to": "SCL", "date_from": "01/03/2024", "date_to": "01/05/2024", "curr": "NZD"}

response = requests.get(url=SERVER, params=params, headers=HEADERS)
print(response.text)
