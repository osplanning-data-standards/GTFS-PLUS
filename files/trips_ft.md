## Additional Transit Vehicle Trip Information

 *  Filename MUST be `trips_ft.txt`
 *  File MUST contain a record for every transit vehicle trip (i.e. the Muni 14 Local Outbound that leaves at 8:02 AM) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`trip_id`			| ID that uniquely identifies a vehicle trip
`vehicle_name`		| Name of vehicle type, which is to match a description in [`vehicles.txt`](vehicles.md)

