## Stop Times

 *  Filename MUST be `stop_times.txt`
 *  File MUST contain a record for every scheduled stop within a trip and route (i.e. the time when the Muni 14 Local Outbound that left at 8:02 gets to 24th St. and Mission St)
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`trip_id`			| ID that uniquely identifies trip
`arrival_time`		| Arrival time at a specific stop for a specific trip on a route in HH:MM:SS format measured from midnight.  For trips that span multiple dates, the time should be entered as a value greater than 240000
`departure_time`	| Departure time at a specific stop for a specific trip on a route in HH:MM:SS format measured from midnight.  For trips that span multiple dates, the time should be entered as a value greater than 240000
`stop_id`			| ID that uniquely identifies a stop
`stop_sequence`		| Sequence number on a specific stop within a trip.  The first stop sequence is 1 and subsequent stops in the trip are sequentially numbered.

File MAY contain the following attributes:

| Optional Attributes		| Description										
| ----------				| -------------		
| `stop_headsign`			| Text that appears on sign that identifies the trips destination to passengers.  Use this field to override default headsign when it changes at stops.
| `pickup_type`			| Type of pickup:
| 						| *0/default - regular pickup*
| 						| *1 - no pickup available*
| 						| *2 - must phone agency*
| 						| *3 - must coordinate with driver*
|`drop_off_type`			| Type of drop off: 
| 						| *0/default - regular drop off*
| 						| *1 - no drop off available*
| 						| *2 - must phone agency*
| 						| *3 - must coordinate with driver*
|`shape_dist_traveled`	| Positions a stop as a distance from the first shape point in units that are used in this field in [`shapes.txt`](shapes.md)
|`timepoint`				| Indicates if specified arrival and departure times for a stop are strictly adhered to by the transit vehicle or if they are approximate and/or interpolated.  
|						| *empty - times considered exact*
| 						| *0 - times considered approximate*
| 						| *1 - times considered exact*
