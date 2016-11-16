## Zones information

 *  Filename MUST be `zones_ft.txt`
 *  File MUST contain a record for every analysis zone.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`zone_id`			| ID that uniquely identifies a zone
`zone_lat`          | Float.  Latitude of zonal centroid or point representing the zone.
`zone_long`         | Float.  Longitude of zonal centroid or point representing the zone.

File MAY contain the following attributes:

Optional Attributes		| Description										
----------				| -------------		
`zone_name`			    | Optional name for identification and display purposes.
