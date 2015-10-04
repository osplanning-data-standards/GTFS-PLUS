## Additional transfer link information
Filename: `transfers_ft.txt`

 *  Filename MUST be `transfers_ft.txt`
 *  File MUST contain a record for each pair of transit stops that can be transferred between 
 on foot.
 *  File MUST contain a record for each Park and Ride:transit stop pair that can be accessed on foot.
 *  File MUST contain a record for each Kiss and Ride:transit stop pair that can be accessed on foot.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`from_stop_id`		| From `stop_id` or park and ride / kiss and ride node.
`to_stop_id`		| To `stop_id` or park and ride / kiss and ride node.
`dist`				| Float walking distance in miles.
`from_route_id`		| To `stop_id` or park and ride / kiss and ride node.
`to_route_id`		| Float walking distance in miles.
`schedule_precedence`| Can be either:
-					 |    from
-					 |    to

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`elevation_gain`	| Integer, feet of the elevation gained along this link.
`population_density`| Float, people per square mile per mile. Can be measured for the area within ¼ mile, or other.
`retail_density`	| Float, employees per square mile per mile. Can be measured for the area within ¼ mile, or other.
`auto_capacity`		| Float, vehicles per hour per mile.  Can be measured for the actual roadway, an area within ¼ mile, or other.
`indirecctness`		| Float, ratio of the manhattan distance to crow-fly distance.
