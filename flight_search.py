import requests
import serpapi
import dotenv import load_dotenv 
load_dotenv()
class FlightSearch:
    def __init__(self):
        self.client = Client(api_key=os.getenv("API_KEY"))
    
    #This class is responsible for talking to the Flight Search API.

### start search left off here why need to create reading part of spread sheet that way we can have inputs to test search not go in blind
    def search(self,)
    results = self.client.search({
        "engine":"google_flights",
        "departure_id": 
    }
    )
    