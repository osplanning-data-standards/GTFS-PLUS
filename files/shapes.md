## Shapes

 *  Filename MUST be `shapes.txt`
 *  File MAY contain a record for shape points in a single shape that collectively describes the path transit vehicles take on their trips.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`shape_id`			| ID that uniquely identifies shape
`shape_pt_lat`		| Latitude of a shape point (WGS 84)
`shape_pt_long`		| Longitude of a shape point (WGS 84)
`shape_pt_sequence`	| Associates the latitude and longitude of a shape point sequence order along a shape

File MAY contain the following attributes:

Optional Attributes		| Description										
----------				| -------------		
`shape_dist_traveled`	| Distance from the first shape point as a real distance in feet

