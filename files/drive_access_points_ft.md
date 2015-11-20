## Drive Access Points
Filename: `drive_access_points_ft.txt`

In order to be connected to the transit system, drive access points must be connected to transit stops in [`transfers_ft.txt`](/files/transfers_ft.md)

 *  Filename MUST be `drive_access_points_ft.txt`
 *  File MUST contain a record for each drive access point such as park and ride lots, hide and ride areas, and kiss and ride drop off areas.
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
`drop_off`			| Boolean, if not specified assumed to be true to indicated that drop-off/pick-ups are allowed.
`capacity`			| Integer.  Represents number of parking spaces at park and ride.  If not specified, assumed to be zero.
`hourly_cost`		| Hourly cost to park in the unit specified by `currency_type` variable in [`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)
`max_cost`			| Maximum daily cost to park  in the unit specified by `currency_type` variable in [`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)
`type`				| String, with possible values of: 
-					|    surface
-					|    underground
-					|    structure
-					|    street


