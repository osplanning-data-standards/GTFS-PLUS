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
`vehicle_name`		| Name of vehicle type, which is to match a description in [`vehicles_ft.txt`](vehicles_ft.md)

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`schedule_time`		| Integer, number of minutes from scheduled `arrival_time` at first stop to scheduled `departure_time` at last stop.
`actual_time`		| Integer, number of minutes from actual `arrival_time` at first stop to actual `departure_time` at last stop.
`schedule_stop_time`| Integer, number of minutes scheduled stop time.
`actual_stop_time`	| Integer, number of minutes actual stop time.
`stop_delay`		| Integer, number of minutes of stop delay.
`schedule_move_time`| Integer, number of minutes scheduled moving time.
`actual_move_time`	| Integer, number of minutes actual moving time.
`move_delay`		| Integer, number of minutes of moving delay.