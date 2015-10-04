## Transit Routes

 *  Filename MUST be `routes.txt`
 *  File MUST contain a record for every transit route (i.e. the Muni 14 Local) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`route_id`			| ID that uniquely identifies a route
`route_short_name`	| Short name of route
`route_long_name`	| Long name of route
`route_type`		| Service Type:
- 					|    *0 - Tram, streetcar, light rail*
- 					|    *1 - Subway, metro*
- 					|    *2 - Rail*
- 					|    *3 - Bus*
- 					|    *4 - Ferry*
- 					|    *5 - Cable car*
- 					|    *6 - Gondola*
- 					|    *7 - Funicular*

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`agency_id`			| ID that uniquely identifies an agency in [`agency.txt`](agency,md)
`route_desc`		| Description of route.
`route_url`			| Webpage for route.
`route_color`		| Display color for route in six digit hexadecimal
`route_text_color`	| Color of text to be drawn on top of route color, specified in six digit hexadecimal
