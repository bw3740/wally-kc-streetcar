## KC Streetcar
Retrieves estimates for next Kansas City streetcar arrival times in both directions.

## Description 
Based on a configurable static stop, this skill retrieves the number of minutes until the next streetcars arrive in either the North or South directions. 

Information is provided free-of-charge from http://www.kc-metro.com/tmwebwatch/LiveArrivalTimes. This page, with a routeID and directionID, makes to POST calls to http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStops to get a list of stops and http://www.kc-metro.com/tmwebwatch/Arrivals.aspx/getStopTimes to get the arrival times for a specific stop. Keep in mind some intersections have 2 stops, so direction matters.

This skill is still in it's early stages of development. With the planned expansions of the line, there will be tweaks needed. This is for the good of the KC and Mycroft communities, so please add/suggest new features.

## Example Intents
* "kc street car at third" 
* "kansas city streetcar at ninth heading north"

## List of Supported Stops
* 3rd & Grand = "third" or "grand"
* 4th & Delaware = "fourth" or "delaware"
* 5th & Walnut = "fifth" or "walnut"
* 7th & Main = "seventh"
* 9th & Main = "ninth"
* 12th & Main = "twelfth"
* 14th & Main = "fourteenth"
* 16th & Main = "sixteenth"
* 19th & Main = "nineteenth"
* Union Station = "union" or "station"

## Future Enhancements
* Prompt user for "North" or "South" if they don't specify it for bi-directional stops

## Credits 
Brad Walters & Matt Burke @ The Nerdery