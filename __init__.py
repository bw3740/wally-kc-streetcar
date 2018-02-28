import json
import requests

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'Brad Walters @ The Nerdery'

#Transit Master URL
URL = 'http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes'
HEADERS = {'Content-Type': 'application/json'}

#contants
NORTH = 14
SOUTH = 15
ROUTE_ID = 100
THIRD_STREET_NORTH = 9215
FOURTH_STREET_SOUTH = 9230
FIFTH_STREET_NORTH = 9237
SEVENTH_STREET_NORTH = 9138
SEVENTH_STREET_SOUTH = 9132
NINTH_STREET_NORTH = 9137
NINTH_STREET_SOUTH = 9133
TWELFTH_STREET_NORTH = 9236
TWELFTH_STREET_SOUTH = 9231
FOURTEENTH_STREET_NORTH = 9235
FOURTEENTH_STREET_SOUTH = 9232
SIXTEENTH_STREET_NORTH = 9234
SIXTEENTH_STREET_SOUTH = 9233
NINETEENTH_STREET_NORTH = 9136
NINETEENTH_STREET_SOUTH = 9134
UNION_STATION_SOUTH = 9135

LOGGER = getLogger(__name__)

class KCStreetcarSkill(MycroftSkill):
    def __init__(self):
        super(KCStreetcarSkill, self).__init__(name="KCStreetcarSkill")
        self.process = None

    @intent_handler(IntentBuilder("ThirdAndGrand")
        .require("KCStreetcarIntent")
        .require("ThirdAndGrand").build())
    def handle_third_and_grand_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':THIRD_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "", "stop": "third and grand", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR ThirdAndGrand: {0}".format(e))

    @intent_handler(IntentBuilder("FourthAndDelaware")
        .require("KCStreetcarIntent")
        .require("FourthAndDelaware").build())
    def handle_fourth_and_delaware_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':FOURTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "", "stop": "fourth and delaware", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR FourthAndDelaware: {0}".format(e))

    @intent_handler(IntentBuilder("FifthAndWalnut")
        .require("KCStreetcarIntent")
        .require("FifthAndWalnut").build())
    def handle_fifth_and_walnut_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':FIFTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "", "stop": "fifth and walnut", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR FifthAndWalnut: {0}".format(e))

    @intent_handler(IntentBuilder("SeventhAndMainNorth")
        .require("KCStreetcarIntent")
        .require("SeventhAndMain")
        .require("North").build())
    def handle_seventh_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':SEVENTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "seventh and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR SeventhAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("SeventhAndMainSouth")
        .require("KCStreetcarIntent")
        .require("SeventhAndMain")
        .require("South").build())
    def handle_seventh_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':SEVENTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "seventh and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR SeventhAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("NinthAndMainNorth")
        .require("KCStreetcarIntent")
        .require("NinthAndMain")
        .require("North").build())
    def handle_ninth_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':NINTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "ninth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR NinthAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("NinthAndMainSouth")
        .require("KCStreetcarIntent")
        .require("NinthAndMain")
        .require("South").build())
    def handle_ninth_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':NINTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "ninth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR NinthAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("TwelfthAndMainNorth")
        .require("KCStreetcarIntent")
        .require("TwelfthAndMain")
        .require("North").build())
    def handle_twelfth_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':TWELFTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "twelfth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR TwelfthAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("TwelfthAndMainSouth")
        .require("KCStreetcarIntent")
        .require("TwelfthAndMain")
        .require("South").build())
    def handle_twelfth_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':TWELFTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "twelfth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR TwelfthAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("FourteenthAndMainNorth")
        .require("KCStreetcarIntent")
        .require("FourteenthAndMain")
        .require("North").build())
    def handle_fourteenth_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':FOURTEENTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "fourteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR FourteenthAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("FourteenthAndMainSouth")
        .require("KCStreetcarIntent")
        .require("FourteenthAndMain")
        .require("South").build())
    def handle_fourteenth_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':FOURTEENTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "fourteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR FourteenthAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("SixteenthAndMainNorth")
        .require("KCStreetcarIntent")
        .require("SixteenthAndMain")
        .require("North").build())
    def handle_sixteenth_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':SIXTEENTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "sixteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR SixteenthAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("SixteenthAndMainSouth")
        .require("KCStreetcarIntent")
        .require("SixteenthAndMain")
        .require("South").build())
    def handle_sixteenth_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':SIXTEENTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "sixteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR SixteenthAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("NineteenthAndMainNorth")
        .require("KCStreetcarIntent")
        .require("NineteenthAndMain")
        .require("North").build())
    def handle_nineteenth_and_main_north_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':NORTH,'stopID':NINETEENTH_STREET_NORTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading north", "stop": "nineteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR NineteenthAndMainNorth: {0}".format(e))

    @intent_handler(IntentBuilder("NineteenthAndMainSouth")
        .require("KCStreetcarIntent")
        .require("NineteenthAndMain")
        .require("South").build())
    def handle_nineteenth_and_main_south_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':NINETEENTH_STREET_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "heading south", "stop": "nineteenth and main", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR NineteenthAndMainSouth: {0}".format(e))

    @intent_handler(IntentBuilder("UnionStation")
        .require("KCStreetcarIntent")
        .require("UnionStation").build())
    def handle_union_station_intent(self, message):
        try:
            nextTime = self.process_request({'routeID':ROUTE_ID,'directionID':SOUTH,'stopID':UNION_STATION_SOUTH,'useArrivalTimes':'true'})
            self.speak_dialog("next_car", {"direction": "", "stop": "union station", "nextTime": nextTime})
        except Exception as e:
            LOGGER.error("ERROR UnionStation: {0}".format(e))

    def process_request(self, payload):
        try:
            response = requests.post(URL, data=json.dumps(payload), headers=HEADERS)
            jsonObject = response.json()

            #TODO: check for null values
            crossing = jsonObject['d']['routeStops'][0]['stops'][0]['crossings'][0]
            #LOGGER.info(crossing)

            #TODO: handle delays and cancellations
            #TODO: integrate dialog for time and direction
            
            return "{0} {1}".format(crossing['predTime'], crossing['predPeriod'])

        except Exception as e:
            LOGGER.error("ERROR process_request: {0}".format(e))

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return KCStreetcarSkill()
