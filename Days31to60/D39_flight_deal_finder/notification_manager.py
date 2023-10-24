from config import TELEGRAM_BOT_KEY, CHAT_ID
import requests


class NotificationManager:

    def __init__(self):
        pass
        # self.new_message = new_message

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url).json()  # this sends the message


# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())
