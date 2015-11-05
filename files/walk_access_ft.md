## Walk Access Links
Filename: `walk_access_ft.txt`

 *  Filename MUST be `walk_access_ft.txt`
 *  File MUST contain a record for each transit stop that can be walked to from each TAZ.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`taz`				| Zone ID
`stop_id`			| Stop ID
`dist`				| Walking distance in miles between TAZ and stop.

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`elevation_gain`	| Integer, feet of the elevation gained along this link.
`population_density`| Float, people per square mile per mile. Can be measured for the area within ¼ mile, or other.
`retail_density`	| Float, employees per square mile per mile. Can be measured for the area within ¼ mile, or other.
`auto_capacity`		| Float, vehicles per hour per mile.  Can be measured for the actual roadway, an area within ¼ mile, or other.
`indirecctness`		| Float, ratio of manhattan distance to crow-fly distance.