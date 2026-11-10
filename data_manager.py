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
        list__locations = []
        for row in result["sheet1"]:
            list__locations.append((row["id"],row["iataCode"]))

        return list__locations 

    def addprice(self,row_id,price):
        body = {"sheet1":{"lowestPrice":price}}
        response = requests.put(url=f"{self.url}/{row_id}",json=body)
    
    def addlocation(self,city,iata_code,lowestPrice):
        body = {"sheet1":{"city":city,"iataCode":iata_code,"lowestPrice":lowestPrice}}
        response =requests.post(url=self.url,json=body)
        print(response)

    def removelocation():
        pass

        










































































































































