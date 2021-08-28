import requests

from datetime import date
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
import os


class FlightSearch:
    _TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com"
    _TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
    _TEQUILA_AFFIL_ID = os.getenv("TEQUILA_AFFIL_ID")

    _headers = {
        "apikey": _TEQUILA_API_KEY,
    }

    def __init__(self):
        today = date.today()
        six_months = date.today() + relativedelta(months=+6)

        self.today = today.strftime("%d/%m/%Y")
        self.six_months = six_months.strftime("%d/%m/%Y")

    def get_iata_code(self, city_name: str):

        api_url = f"{self._TEQUILA_API_ENDPOINT}/locations/query"

        params = {
            "term": city_name,
            "location_types": "city",
            "limit": 1,
        }

        response = requests.get(api_url, params=params, headers=self._headers)
        response.raise_for_status()

        city_code = response.json()["locations"][0]["code"]

        return city_code

    def get_flight(self, city: dict, from_city: str = "LON", max_stopovers: int = 0) -> FlightData:

        api_url = f"{self._TEQUILA_API_ENDPOINT}/v2/search"

        params = {
            "fly_to": city['iataCode'],
            "fly_from": from_city,
            "date_from": self.today,
            "date_to": self.six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": max_stopovers,
            "curr": "USD"
        }

        response = requests.get(url=api_url, params=params, headers=self._headers)
        response.raise_for_status()

        if max_stopovers == 1:
            print(response.json())

        flight_data = FlightData(json_data=response.json(), lowest_price=city["lowestPrice"], flight_search=self, from_city=from_city, city=city)

        return flight_data

    def get_all_flights(self, data: list) -> list[FlightData]:
        flight_data_list = []
        for city in data:
            flight_data = self.get_flight(city)
            flight_data_list.append(flight_data)

        return flight_data_list
