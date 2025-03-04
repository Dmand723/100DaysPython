#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from classes.data_manager import DataManager
from classes.flight_search import FlightSearch
from classes.flight_data import FlightData
from classes.notification_manager import NotificationManager
import time
from datetime import datetime, timedelta

dataManager = DataManager()
sheetData = dataManager.getDestinationData()
flightSearch = FlightSearch()

ORIGIN_CITY_IATA = 'SLC'

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary
if sheetData[0]['iataCode'] == "":
    
    for row in sheetData:
        row["iataCode"] = flightSearch.getDestinationCode(row['city'])

        time.sleep(2)
    print(f"sheetData:\n {sheetData}")

    dataManager.destination_data = sheetData
    dataManager.updateDestinationCodes()

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheetData:
    print(f"Getting flights for {destination['city']}...")
    flights = flightSearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = FlightData.find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)