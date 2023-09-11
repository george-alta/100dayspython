from config import NEWSAPI_KEY
from messages import send_message
import requests


def getnews():
    parameters = {"q": "tesla",
                  "apiKey": NEWSAPI_KEY,
                  "pageSize": 10}

    response2 = requests.get(
        "https://newsapi.org/v2/everything", params=parameters)

    # three_articles = response2.json()["articles"][:3]
    # send_message(three_articles)

    for i in range(3):
        source = response2.json()["articles"][i]["source"]["name"]
        title = response2.json()["articles"][i]["title"].upper()
        published_at = response2.json()["articles"][i]["publishedAt"][:10]
        description = response2.json()["articles"][i]["description"]

        message = f"{i+1}. {title} ({source} reported on {published_at})\n{description}\n"

        print(message)
        send_message(message)
