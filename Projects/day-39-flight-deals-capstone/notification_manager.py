from flight_data import FlightData


class NotificationManager:

    def __init__(self, flights_data: list[FlightData]):
        self.flights_data = flights_data

    def send_messages(self):
        for flight_data in self.flights_data:
            if flight_data.is_lowest:
                print(flight_data.get_message())
