## Kiss and Ride Lots
Filename: `knr.txt`

 *  Filename MUST be `knr.txt`
 *  File MUST contain a record for each kiss and ride lot.
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
