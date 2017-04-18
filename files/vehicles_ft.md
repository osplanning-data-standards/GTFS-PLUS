## Vehicles

 *  Filename MUST be `vehicles_ft.txt`
 *  File MUST contain a record for each vehicle type
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`vehicle_name`		| String that uniquely identifies vehicle type

File MAY contain the following attributes:

|Optional Attributes		| Description										
| ----------				| -------------		
| `vehicle_description`	| String description of the vehicle. For example, "metro-articulated"
| `seated_capacity`		| Integer of total seated capacity per vehicle. If specified, this will override capacity from trip file.
| `standing_capacity`		| Integer of number of standing riders at capacity.  If specified, this will override capacity from trip file.
| `number_of_doors`		| Integer of number of doors.
| `max_speed`				| Float of the maximum speed of the vehicle in miles per hour.
| `vehicle_length`		| Float of the vehicle length in feet.
| `platform_height`		| Float of the platform height in inches.
| `propulsion_type`		| String of the name of the propulsion type.  Possible values include:
|	| diesel
| | bio-diesel
| | diesel-hybrid
| | CNG
|	| electric-trolly
| `wheelchair_capacity`	| Integer of total capacity for wheelchairs on vehicle. Overrides value in trip file.  
|	| Blank - indicates that it is unknown and is treated as infinite.  
| | 0  - indicates that wheelchairs cannot access this vehicle.
| | 1+ - number of wheelchairs that can be accommodated
| `bicycle_capacity`		| Integer representation of [non-folding] bicycles that can be accommodated.  
|	| Blank - indicates that it is unknown and is treated as infinite unless the trip file says that it is not bicycle accessible.
|	| 0  - indicates that bicycles cannot ride on this vehicle.
|	| 1+ - number of bicycles that can be accommodated
