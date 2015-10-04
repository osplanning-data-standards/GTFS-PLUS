## Transit Vehicle Trips

 *  Filename MUST be `trips.txt`
 *  File MUST contain a record for every transit vehicle trip (i.e. the Muni 14 Local Outbound that leaves at 8:02 AM) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`trip_id`			| ID that uniquely identifies a vehicle trip
`route_id`			| ID that uniquely identifies a route
`service_id`		| ID that uniquely identifies set of dates when service is available from calendar or calendar dates files.

File MAY contain the following attributes:

Optional Attributes		| Description										
----------				| -------------		
`trip_headsign`			| Text that appears on the vehicle headsign to identify destination to passengers.
`trip_short_name`		| Text that appears in schedules and sign boards.
`block_id`				| Two or more sequential trips made using same vehicle where passenger can transfer by staying on same vehicle. `block_id` must be referenced by two or more trips in trips.txt.
`shape_id`				| Defines shape for the trip from [`shapes.txt`](shapes.md) file.
`wheelchair_accessible`	| Is this transit vehicle trip wheelchair accessible: 
				    -	|	  *0 - no accessibility info*
					-	|	  *1 - vehicle on this trip can accommodate at least one rider in a wheelchair*
					-	|	  *2 - no riders in wheelchairs can be accommodated on this trip* 
`bikes_allowed`			| Does this transit vehicle trip bike allow bikes:
				    -	|	  *0 - no bike accessibility info*
				    -	|	  *1 - vehicle on this trip can accommodate at least one bicycle*		
				    -	|	  *2 - no bicycles can be accommodated on this trip*		    
`direction_id`			| ID that contains a binary value that indicates the direction of the trip:
				    -	|	  *0 - travel in one direction*
				    -	|	  *1 - travel in opposite direction*	

