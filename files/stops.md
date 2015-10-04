## Stops 

 *  Filename MUST be `stops.txt`
 *  File MUST contain a record for every transit stop or station (i.e. Embarcadero Station) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`stop_id`			| ID that uniquely identifies a stop
`stop_name`			| Name of stop or station
`stop_lat`			| Latitude of stop or station in WGS 84
`stop_lon`			| Longitude of stop or station in WGS 84

File MAY contain the following attributes:

Optional Attributes		| Description										
----------				| -------------		
`stop_code`				| Short text or a number that identifies the stop for passengers (i.e. EMB)
`stop_desc`				| Description of stop or station
`zone_id`				| Defines a fare zone for the stop ID. Required if you want to provide fare information in [`fare_rules.txt`](fare_rules.md) that uses zones.
`location_type`			| Identifies whether this stop is a stop or station.  If nothing is specified or is blank, it is assumed it is a stop.  Stations can have different properties from stops.
- 						| *0 or blank - stop*
- 						| *1 - station (contains one or more stops)*
`parent_station`		| For stops inside stations, identifies station associated with the stop.  `Stops.txt` must also contain a row where this stop id is assigned a location type 1.
`stop_timezone`			| Contains timezone where stop or station is located.  If omitted, stop assumed to be located in timezone in [`agency.txt`](agency.md).
`wheelchair_boarding`	| Identifies whether wheelchair boardings are possible from the specified stop or station. 
- 						| *0 - no information*
- 						| *1 - some vehicles can be boarded by wheelchair*
- 						| *2 - wheelchair boarding not possible*
- 						| If the stop is part of the station:
- 						| *0 - will inherit from parent station, if specified.*
- 						| *1 - there is an accessible path from outisde station to stop*
- 						| *2 - no accessible path to specific stop*

