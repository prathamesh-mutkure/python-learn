import requests
from flight_search import FlightSearch
import os


class DataManager:

    _SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
    _SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

    _headers = {
        "Authorization": f"Bearer {_SHEETY_BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    def __init__(self, flights_search: FlightSearch):
        self.flights_search = flights_search
        self.sheet_data = []
        self.read_sheet()

    def read_sheet(self) -> dict:
        response = requests.get(self._SHEETY_API_ENDPOINT, headers=self._headers)
        response.raise_for_status()

        self.sheet_data = response.json()["prices"]

        return response.json()

    def update_row_iata_code(self, row_id, iata_code):
        api_url = f"{self._SHEETY_API_ENDPOINT}/{row_id}"

        json_data = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(api_url, json=json_data, headers=self._headers)
        response.raise_for_status()

        return response.status_code

    def populate_iata_codes(self):

        for row in self.sheet_data:
            code = self.flights_search.get_iata_code(row["city"])
            response_code = self.update_row_iata_code(row_id=row["id"], iata_code=code)

            print(response_code)
