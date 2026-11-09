import requests
import os 
from dotenv import load_dotenv 
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.getenv("SHEETY_URL")
    
    def locations(self):
        location = requests.get(url=self.url)
        result = location.json()
        # ex = result["city"]
        flocation = result["sheet1"][0]["iataCode"]

        return flocation 

    def addprice(self,row_id,price):
        body = {"sheet1":{"lowestPrice":price}}
        response = requests.put(url=f"{self.url}/{row_id}",json=body)
    
    def addlocation(self):
        











































































































































