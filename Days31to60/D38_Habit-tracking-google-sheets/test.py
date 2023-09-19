
import requests

GENDER = 'male'
WEIGHT_KG = '80'
HEIGHT_CM = '176'
AGE = '38'

APP_ID = 'f28014ca'
API_KEY = '17fa8464ef8a4ecdcf28ddde45504084'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
