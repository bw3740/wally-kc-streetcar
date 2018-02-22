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

            #TODO: make stop and direction inputs the user chooses beforehand
            postData = json.JSONEncoder().encode({'routeID':100,'directionID':15,'stopID':9138,'useArrivalTimes':true})
            response = requests.post(url, postData)
            jsonData = json.load(response.data)
            #TODO: check for null values
            nextStop = jsonData.d.routeStops[0].stops[0].crossings[0]
            
            #TODO: integrate dialog
            self.speak_dialog('The next streetcar will arrive at ' + nextStop.predTime + ' ' + nextStop.predPeriod)

        except Exception as e:
            LOGGER.error("Error: {0}".format(e))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return KCStreetcarSkill()