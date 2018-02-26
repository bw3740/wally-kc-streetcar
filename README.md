## KC Streetcar
Retrieves estimates for next Kansas City streetcar arrival times in both directions.

## Description 
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions. 

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page, with a routeID and directionID, makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop. Keep in mind some intersections have 2 stops, so direction matters.

For reference, here are the routeID and directionID's needed for to produce the list below:
* routeID:100
* directionID: North 14: South 15

Below is a list of stopID's for the different stops:

* 3rd & Grand: 9215
* 4th & Delaware: 9230
* 5th & Walnut: 9237
* 7th & Main: North 9138: South 9132
* 9th & Main: North 9137: South 9133
* 12th & Main: North 9236: South 9231
* 14th & Main: North 9235: South 9232
* 16th & Main: North 9234: South 9233
* 19th & Main: North 9136: South 9134
* Union Station: 9135

This skill is still in it's early stages of development. It is hard-coded to Southbound 7th & Main St until settings can be implemented. This is for the good of the KC and Mycroft communities, so please add/suggest new features.

## Example Intents
### Current Intents
* next street car
* next kansas city streetcar"
### Future Intents
* "next north street car"
* "next south kansas city streetcar"

## Credits 
Brad Walters @ The Nerdery