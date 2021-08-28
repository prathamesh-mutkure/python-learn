# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flights_search = FlightSearch()
data_manager = DataManager(flights_search=flights_search)
flights_data = flights_search.get_all_flights(data=data_manager.sheet_data)

notification_manager = NotificationManager(flights_data=flights_data)
notification_manager.send_messages()
