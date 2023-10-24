# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# insert telegram API

ORIGIN_CITY_IATA = "AKL"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
