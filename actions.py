# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from youtubesearchpython import VideosSearch

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         slot_value = next(tracker.get_latest_entity_values("issue_keyword"),None)
         videoSearch =  VideosSearch(slot_value,limit=1)
         title = videoSearch.result()['result'][0]['title']
         result = videoSearch.result()['result'][0]['link']
         dispatcher.utter_message(text = title)
         dispatcher.utter_message(text= result)


         return []
