import requests
import os
import serpapi
from dotenv import load_dotenv 
load_dotenv()
class FlightSearch:
    def __init__(self):
        self.client = serpapi.Client(api_key=os.getenv("API_KEY"))
    
    #This class is responsible for talking to the Flight Search API.

### start search left off here why need to create reading part of spread sheet that way we can have inputs to test search not go in blind
    def search(self,destenation_code):
        results = self.client.search({
        "engine":"google_flights",
        "departure_id":"SFO",
        "arrival_id":destenation_code,
        "currency":"USD",
        "type": "2",
        "outbound_date": "2026-11-20",
        "sort_by": 2,

    }
    )   
        top = results["other_flights"][0]
        name = top["flights"][-1]["arrival_airport"]["name"]
        print(name)
        print(f"Price for flight ${top["price"]} lowest price yet!")

        return top["price"]
