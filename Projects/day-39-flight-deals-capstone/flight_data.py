
class FlightData:

    def __init__(self, json_data, lowest_price, flight_search, city: dict, from_city):
        try:
            data = json_data["data"][0]
        except IndexError:
            self.is_lowest = False

            # flight_data_new = flight_search.get_flight(max_stopovers=1, from_city=from_city, city=city)
            # self.__dict__.update(flight_data_new.__dict__)
            # self.max_stopovers = 1
        else:
            self.from_city = data["cityFrom"]
            self.to_city = data["cityTo"]
            self.city_code_from = data["cityCodeFrom"]
            self.city_code_to = data["cityCodeTo"]
            self.price = data["price"]
            self.lowest_price = lowest_price
            self.is_lowest = self.price <= lowest_price
            self.local_departure = data["local_departure"].split("T")[0]

    def get_message(self) -> str:
        return "Lowest Price Alert!\n" \
               f"Only ${self.lowest_price} to fly from {self.from_city} to {self.to_city}\n" \
               f"Date: {self.local_departure}\n"
