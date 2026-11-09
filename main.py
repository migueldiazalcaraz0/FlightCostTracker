#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
import os 
import serpapi
from datetime import datetime
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()





dm = DataManager()
code = dm.locations()


search = FlightSearch()
results = search.search(code)


addprice = dm.addprice(3,results)

# print(code)