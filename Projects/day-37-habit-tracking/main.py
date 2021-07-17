import requests
import random
from datetime import datetime
import os

PIXELA_ENDPOINT = "https://pixe.la/v1"
USERNAME = "prathamesh-m009"
TOKEN = os.getenv("TOKEN")
GRAPH_NAME = "graph-cycle"

headers = {
    "X-USER-TOKEN": TOKEN,
}


def create_user():
    api_url = f"{PIXELA_ENDPOINT}/users"

    json_data = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(api_url, json=json_data)
    response.raise_for_status()

    return response.json()


def create_graph():
    api_url = f"{PIXELA_ENDPOINT}/users/{USERNAME}/graphs"

    json_data = {
        "id": GRAPH_NAME,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai",
    }

    response = requests.post(api_url, json=json_data, headers=headers)
    response.raise_for_status()

    print(response.json())

    return response


def add_pixel(date: datetime = datetime.now(), quantity: str = str(random.randint(0, 20))):
    api_url = f"{PIXELA_ENDPOINT}/users/{USERNAME}/graphs/{GRAPH_NAME}"

    date_string = date.strftime("%Y%m%d")

    json_data = {
        "date": date_string,
        "quantity": quantity,
    }

    response = requests.post(api_url, json=json_data, headers=headers)
    response.raise_for_status()

    print(response.json())

    return response.json()


def update_pixel(data_string: str, quantity: str = str(random.randint(0, 20))):
    api_url = f"{PIXELA_ENDPOINT}/users/{USERNAME}/graphs/{GRAPH_NAME}/{data_string}"

    json_data = {
        "date": data_string,
        "quantity": quantity,
    }

    response = requests.put(api_url, json=json_data, headers=headers)
    response.raise_for_status()

    print(response.json())

    return response.json()


def delete_pixel(date_string: str):
    api_url = f"{PIXELA_ENDPOINT}/users/{USERNAME}/graphs/{GRAPH_NAME}/{date_string}"

    response = requests.delete(api_url, headers=headers)
    response.raise_for_status()

    print(response.json())

    return response.json()


# create_user()
# create_graph()
# add_pixel()
# update_pixel("20210717")
# delete_pixel("20210717")
