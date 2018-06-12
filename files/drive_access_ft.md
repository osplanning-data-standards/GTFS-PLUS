## Drive Access Links
Filename: `drive_access_ft.txt`

 *  Filename MUST be `drive_access_ft.txt`
 *  File MUST contain a record for each park and ride/kiss and ride that can be driven to from each TAZ.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`taz`				    | Zone ID
`lot_id`			  | Stop ID
`direction`			| String that can have following values:
`-`				  	  |    Access
`-`	    		    |    Egress
`dist`				  | Float. Drive distance in miles between TAZ and lot.
`cost`				  | Float. Cost in the unit specified by `currency_type` variable in [`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)
`travel_time`		| Float. Driving time in minutes between TAZ and lot.
`start_time`		| HH:MM:SS from midnight.  If blank, it is assumed that this is the base condition and other time of days will override it.
`end_time`			| HH:MM:SS from midnight.  Time when drive access link is no longer valid (i.e. if it ends at 11:59:59, then `end_time` would be 12:00:00) If blank, it is assumed that this is the base condition and other time of days will override it.

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`elevation_gain`	| Integer, feet of the elevation gained along this link.
`population_density`| Float, people per square mile per mile. Can be measured for the area within ¼ mile, or other.
`retail_density`	| Float, employees per square mile per mile. Can be measured for the area within ¼ mile, or other.
`auto_capacity`		| Float, vehicles per hour per mile.  Can be measured for the actual roadway, an area within ¼ mile, or other.
`indirectness`		| Float, ratio of the manhattan distance to crow-fly distance.
