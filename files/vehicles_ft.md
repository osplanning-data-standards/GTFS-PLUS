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
| `seated_capacity`		| Integer of total seated capacity per vehicle. 
| `standing_capacity`	| Integer of number of standing riders at capacity.  
| `number_of_doors`		| Integer of number of doors.
| `max_speed`			| Float of the maximum speed of the vehicle in miles per hour.
| `vehicle_length`		| Float of the vehicle length in feet.
| `platform_height`		| Float of the platform height in inches.
| `propulsion_type`		| String of the name of the propulsion type.  Possible values include:
|	| `diesel`
| | `bio-diesel`
| | `diesel-hybrid`
| | `CNG`
|	| `electric-trolly`
| `wheelchair_capacity`	| Integer of total capacity for wheelchairs on vehicle. Overrides value in trip file.  
|	| `Blank` - indicates that it is unknown and is treated as infinite.  
| | `0`  - indicates that wheelchairs cannot access this vehicle.
| | `1+` - number of wheelchairs that can be accommodated
| `bicycle_capacity`		| Integer representation of [non-folding] bicycles that can be accommodated.  
|	| `Blank` - indicates that it is unknown and is treated as infinite unless the trip file says that it is not bicycle accessible.
|	| `0`  - indicates that bicycles cannot ride on this vehicle.
|	| `1+` - number of bicycles that can be accommodated
| `boarding_door` | String value identifying the door(s) used for boarding. This is a TCQSM parameter used to calculate dwell time.
| | `Blank` - indicates that it is unknown, assumed to be front door boarding
| | `front` - indicates boarding is only allowed at the front door
| | `all` - indicates boarding is allowed at all doors
| `fare_payment_method` | String value indicating method of payment accepted.  Each method corresponds to a default boarding time value in seconds/passenger. This is a TCQSM parameter used to calculate dwell time.
| | `none` - indicates no fare payment. Default value 1.75 s/p.
| | `visual_inspection` - indicates visual inspection of a paper pass, paper transfer, or mobile phone pass. Default value 2.0 s/p.
| | `single_ticket_token` - indicates a single ticket or token placed into a farebox. Default value 3.0 s/p.
| | `exact_change` - indicates exact change paid into a farebox. Default value 4.5 s/p.
| | `ticket_validator` - indicates a ticket placed into mechanical ticket validator. Default value 4.0 s/p.
| | `magstripe_card` - indicates a magnetic strip card swiped through validator. Default value 5.0 s/p.
| | `smart_card` - indicates a smart card tapped against validator. Default value 2.75 s/p.
| | `user_defined` - if selected, a value should be provided in the `user_defined_fare_payment` field.
| `user_defined_fare_payment` | Floating point representation of boarding time due to the type of fare payment, in seconds/passenger. Should be blank unless `fare_payment_method` is `user_defined`. This is a TCQSM parameter used to calculate dwell time.
| `boarding_height` | String value indicating the boarding height as one of three categories. This is a TCQSM parameter used to calculate dwell time.
| | `level` - indicates the bus floor and loading platform are at the same height.
| | `stairs` - indicates the bus floor is above the loading platform height, and/or there are stairs from the door to the bus floor.
| | `steep_stairs` - indicates there are steep stairs to a bus floor, as typically found on a high-floor commuter bus.
| `door_time` | Integer representation of seconds for doors to open and close, usually between 2 and 5 seconds. This is a TCQSM parameter used to calculate dwell time.
| `acceleration` | Float value indicating the acceleration of the vehicle in miles/hour/second
| `deceleration` | Float value indicating the deceleration of the vehicle in miles/hour/second
| `dwell_formula` | String value containing a formula to calculate dwell time.
