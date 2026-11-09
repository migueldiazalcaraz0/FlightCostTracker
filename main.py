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
        code = dm.locations()
        search = FlightSearch()
        print("Loading...")
        results = search.search(code)
        addprice = dm.addprice(2,results)
    elif answer ==2:
        city = input("Enter City of Intrest: ")
        iata = input("iATA Code: ")
        default_price =  0 
        dm.addlocation(city,iata,default_price)





check_pricing()
# dm = DataManager()
# code = dm.locations()


# search = FlightSearch()
# results = search.search(code)



# print(code)