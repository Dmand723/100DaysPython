import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9641387e59dfa1814de392f6f7fa6695/flightDealsPython/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ['SHEETY_USERNAME']
        self._password = os.environ['SHEETY_PASSWORD']
        self._authorization = HTTPBasicAuth(self._user,self._password)
        self.destination_data = {}

    def getDestinationData(self):
        res = requests.get(url=SHEETY_PRICES_ENDPOINT,auth=self._authorization)
        data =res.json()
        self.destination_data = data['prices']

        return self.destination_data
    
    def updateDestinationCodes(self):
        for city in self.destination_data:
            new_data = {
                'price':{
                    'iataCode':city['iataCode']
                }
            }
            res = requests.put(
                url=f'{SHEETY_PRICES_ENDPOINT}/{city['id']}',
                json=new_data,
                auth=self._authorization
            )
            print(res.text)