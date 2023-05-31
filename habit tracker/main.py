import requests
from datetime import datetime

USERNAME = "newton"
TOKEN = "newtonnarzary123"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Workout Graph",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did u hit in the gym today?"),
}

# response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config)
# print(response.text)

# check on -> https://pixe.la/v1/users/newton/graphs/graph1.html

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

response = requests.post(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)