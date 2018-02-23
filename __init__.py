import json
import requests

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Brad Walters @ The Nerdery'

LOGGER = getLogger(__name__)

class KCStreetcarSkill(MycroftSkill):
    def __init__(self):
        super(KCStreetcarSkill, self).__init__(name="KCStreetcarSkill")
        self.process = None

    def initialize(self):
        intent = IntentBuilder("KCStreetcarIntent").require("next_car").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:
            LOGGER.info('Preparing to get kc streetcar times')

            url = 'http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes'
            headers = {'Content-Type': 'application/json'}

            #Routes for routeID
            #Streetcar:100

            #Directions for directionID
            #North:14
            #South:15

            #Stops for stopID
            #3rd & Grand:9215
            #4th & Delaware:9230
            #7th & Main:9132
            #9th & Main:9133
            #12th & Main:9231
            #14th & Main:9232
            #16th & Main:9233
            #19th & Main:9134
            #Union Station Main St:9135
            
            #TODO: make stopID and directionID persistent settings the user sets in Mycroft Home
            payload = {'routeID':100,'directionID':15,'stopID':9132,'useArrivalTimes':'true'}

            response = requests.post(url, data=json.dumps(payload), headers=headers)
            jsonObject = response.json()

            #TODO: check for null values
            crossing = jsonObject['d']['routeStops'][0]['stops'][0]['crossings'][0]
            
            #TODO: handle delays and cancellations
            #TODO: integrate dialog for time and direction
            self.speak_dialog('The next streetcar will arrive at ' + crossing['predTime'] + ' ' + crossing['predPeriod'])

        except Exception as e:
            LOGGER.error("Error: {0}".format(e))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return KCStreetcarSkill()