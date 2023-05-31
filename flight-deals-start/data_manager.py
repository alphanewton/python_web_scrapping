import requests

SHEETY_ENDPOINT = "https://api.sheety.co/f244aa6da3b13bc81798d4038dff9d21/flightDealsFinder/prices"


class DataManager:

    def __init__(self):
        self.destination_data = []
        self.customer_data = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()["prices"]
        self.destination_data = data
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        url = "https://api.sheety.co/f244aa6da3b13bc81798d4038dff9d21/flightDealsFinder/users"
        response = requests.get(url=url)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data