## Bike Access Links
Filename: `bike_access_ft.txt`

 *  Filename MUST be `bike_access_ft.txt`
 *  File MUST contain a record for each transit stop that can be biked to from each TAZ.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`taz`				| Zone ID
`stop_id`			| Stop ID
`dist`				| Biking distance in miles between TAZ and stop.

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`elevation_gain`	| Integer, feet of the elevation gained along this link.
`retail_density`	| Float, employees per square mile per mile. Can be measured for the area within ¼ mile, or other.
`auto_capacity`		| Float, vehicles per hour per mile.  Can be measured for the actual roadway, an area within ¼ mile, or other.
`path_dist`			| Float, distance in miles that is a completely separated bike path.
`cycletrack_dist`	| Float, distance in miles that is an on-street separated cycletrack.
`bike_lane_dist`	| Float, distance in miles that is in a bike lane.
`bike_route_dist`	| Float, distance in miles that is a signed bike route.
`num_left_turns`	| Integer, number of left turns.
`num_right_turns`	| Integer, number of right turns.
`num_thru`			| Integer, number of intersections that are thru.
`num_signals`		| Integer, number of traffic signals along route.
