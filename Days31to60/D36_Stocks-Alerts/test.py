import requests
from config import ALPHA_VANTAGE_KEY

# Alpha Vantage API key
# api_key = "YOUR_API_KEY"

# API endpoint URL
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=compact&apikey={ALPHA_VANTAGE_KEY}"

# Make the API request
response = requests.get(url)

# Extract the data from the response
data = response.json()

# Get the last 10 days of stock prices
time_series = data["Time Series (Daily)"]
last_10_days = list(time_series.keys())[:10]

# Print the stock prices for the last 10 days
for day in last_10_days:
    close_price = time_series[day]["4. close"]
    print(f"{day}: {close_price}")
