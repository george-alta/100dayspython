import requests
from config import TELEGRAM_BOT_KEY, CHAT_ID

message = 'this is a test message 🚗'

url = f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/getUpdates"
print(requests.get(url).json())


url = f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage?chat_id={CHAT_ID}&text={message}"
requests.get(url).json()  # this sends the message
