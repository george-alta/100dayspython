import smtplib
import datetime as dt
import csv
import random
from config import my_email, password

now = dt.datetime.now()  # current day and time
day_of_week = now.weekday()
if day_of_week == 4:
    with open('D32_SMTP-Birthday-Reminder/quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        print(all_quotes)
        quote = random.choice(all_quotes)
        print(f"this is a quote: {quote}")
        with smtplib.SMTP("smtp.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="h100dayspythontestingnow@myyahoo.com",
                                msg=f"Subject:get inspired\n\n{quote}")
            print("mail sent")
