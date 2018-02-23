## Nerdery KC Streetcar
Retrieves estimates for next Kansas City streetcar arrival times in both directions.

## Description 
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions. 

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop.

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