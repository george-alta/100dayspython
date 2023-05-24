import requests
QUESTIONS = 10
PARAM = {"amount": QUESTIONS + 1, "type": "boolean"}

response = requests.get("https://opentdb.com/api.php?", params=PARAM)
response.raise_for_status()
data = response.json()

question_data = data["results"]
