# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests


class ActionCheckSafeLocation(Action):
    def name(self) -> Text:
        return "action_check_safe_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to determine if the user is safe
        dispatcher.utter_message(text="Are you currently in a safe location?")
        return []

class ActionGuideUserToSafety(Action):
    def name(self) -> Text:
        return "action_guide_user_to_safety"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = tracker.get_slot('location')
        if location == 'ground floor':
            dispatcher.utter_message(text="Move to higher ground immediately if you can. Avoid walking through floodwaters.")
        else:
            dispatcher.utter_message(text="Stay on the second floor and avoid windows. Keep essential items with you.")
        
        return []

class ActionFindReliefCenter(Action):
    def name(self) -> Text:
        return "action_find_relief_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Logic to find the nearest relief center
        BASE_URL = "http://ipinfo.io/json"
        res = requests.get(BASE_URL)
        res = res.json()
        
        if(res['loc']):
            output = res['loc']
            latitude, longitude = output.split(',')
            latitude = float(latitude)
            longitude = float(longitude)
            
            # Overpass API endpoint with a 5km radius around the coordinates
            url = "https://overpass-api.de/api/interpreter"
            # Overpass QL query to find shelters within 5km radius of the given location
            query = f"""
            [out:json];
            node
            [amenity=shelter](around:5000,{latitude},{longitude});
            out body;
            """
            
            # Making the request to the Overpass API
            response = requests.get(url, params={'data': query})
            data = response.json()
            
            dispatcher.utter_message(text="The nearest relief centers to you are located at: ")

            # Extract and print relevant information
            for element in data['elements']:
                if 'tags' in element:
                    name = element['tags'].get('amenity')
                    lat = element['lat']
                    lon = element['lon']
                    dispatcher.utter_message(text=f"Amenity Type: {name}")
                    dispatcher.utter_message(text=f"Location: {lat}, {lon}\n")
        return []

class ActionProvideEmotionalSupport(Action):
    def name(self) -> Text:
        return "action_provide_emotional_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="It’s okay to feel scared. I’m here with you, and we’ll get through this together.")
        return []

