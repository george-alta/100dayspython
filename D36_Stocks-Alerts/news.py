from config import NEWSAPI_KEY
import requests


def getnews():
    parameters = {"q": "tesla",
                  "apiKey": NEWSAPI_KEY,
                  "pageSize": 10}

    response2 = requests.get(
        "https://newsapi.org/v2/everything", params=parameters)

    for i in range(6):
        source = response2.json()["articles"][i]["source"]["name"]
        title = response2.json()["articles"][i]["title"].upper()
        published_at = response2.json()["articles"][i]["publishedAt"][:10]
        description = response2.json()["articles"][i]["description"]

        print(
            f"{i+1}. {title} ({source} reported on {published_at})\n{description}\n")
