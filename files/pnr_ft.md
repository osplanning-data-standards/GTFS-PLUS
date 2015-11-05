## Park and Ride Lots
Filename: `pnr_ft.txt`

 *  Filename MUST be `pnr_ft.txt`
 *  File MUST contain a record for each park and ride lot.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`lot_id`			| Stop ID
`lot_lat`			| Float.  Lot location latitude in WGS 84
`lot_long`			| Float.  Lot location longitude in WGS 84

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`name`				| String name of the lot.
`capacity`			| Integer.  Represents number of parking spaces at park and ride.  If not specified, assumed to be infinite
`overflow_capacity`	| Integer.  Represents “hide and ride” or unofficial parking availability in surrounding area.  If not specified, assumed to be zero.  
`hourly_cost`		| Integer, cents.  Hourly cost to park.
`max_cost`			| Integer, cents. Maximum daily cost to park.
`type`				| String, with possible values of: 
-					|    surface
-					|    underground
-					|    structure
