from config import NUT_APP_ID, NUT_API_KEY, SHEETY_ENDPOINT
import requests
from datetime import datetime

query = input('what did you do today?: ')

excercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
json_exercise = {
    "query": query,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 176,
    "age": 38
}
headers = {'x-app-id': NUT_APP_ID,
           'x-app-key': NUT_API_KEY,
           'Content-Type': 'application/json'

           }


response = requests.post(url=excercise_endpoint,
                         json=json_exercise, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

json_post = {
    'workout': {
        'date': datetime.now().strftime("%d/%m/%Y"),
        'time': datetime.now().strftime("%H:%M:%S"),
        'exercise': result['exercises'][0]['name'],
        'duration': result['exercises'][0]['duration_min'],
        'calories': result['exercises'][0]['nf_calories']
    }
}

print(json_post)
response2 = requests.post(url=SHEETY_ENDPOINT, json=json_post)
print(response2.text)

# TODO send as date, and time instead of text starting with '
