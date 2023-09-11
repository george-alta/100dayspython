from config import ALPHA_VANTAGE_KEY
from news import getnews
from messages import send_message
import requests
import datetime
import math


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

API_ALPHA = "https://www.alphavantage.co/query"
PARAM_ALPHA = {"function": "TIME_SERIES_INTRADAY",
               "symbol": "TSLA",
               "interval": "60min",
               "outputsize": "compact",
               "apikey": ALPHA_VANTAGE_KEY}
response = requests.get(url=API_ALPHA, params=PARAM_ALPHA)
data1 = response.json()
# print(data1)

last_refresh = response.json()["Meta Data"]["3. Last Refreshed"]
converted_datetime = datetime.datetime.strptime(
    last_refresh, "%Y-%m-%d %H:%M:%S")
yesterday_datetime = converted_datetime - datetime.timedelta(days=5)
yesterday_refresh = yesterday_datetime.strftime("%Y-%m-%d %H:%M:%S")

last_close_price = float(response.json()["Time Series (60min)"][last_refresh]["4. close"])
yesterday_close_price = float(response.json()["Time Series (60min)"][yesterday_refresh]["4. close"])

message = f"🚗 TESLA 🚗 stock checker\ntoday price is ${last_close_price} at {last_refresh}.\nYesterday was {yesterday_close_price} at {yesterday_refresh}"
print(message)
send_message(message)


difference = math.fabs(yesterday_close_price-last_close_price)
percentage_variation = round(difference / yesterday_close_price, 3)
if percentage_variation > 0:
    variation_icon = '🔺'
else:
    variation_icon = '🔻'
    
if percentage_variation > 0.005:
    message =  f"the change was {variation_icon} {percentage_variation*100}%.\nLet's check the news...\n"
    print(message)
    send_message(message)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    getnews()

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
## instead of twilio I am using telegram API

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
