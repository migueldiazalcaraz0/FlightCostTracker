#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
import os 
import serpapi
from datetime import datetime
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()


def check_pricing():
    print("Welcome User To Pricecheck version 1.0 what would you like to do today?")
    print("1. Check Pricing for all locations")
    print("2. Add a new location")
    answer = int(input())
    if answer == 1:
        dm = DataManager()
        rows = dm.locations()
        search = FlightSearch()
        print("Loading...")
        for row_id,code in rows:
            price = search.search(code)
            dm.addprice(row_id,price)
    elif answer ==2:
        city = input("Enter City of Intrest: ")
        iata = input("iATA Code: ")
        default_price =  0 
        dm = DataManager()
        dm.addlocation(city,iata,default_price)
        print("Added Succesfuly! Run option 1 for pricing!")
    else:
        print("good bye jackass")






check_pricing()
# dm = DataManager()
# code = dm.locations()


# search = FlightSearch()
# results = search.search(code)



# print(code)