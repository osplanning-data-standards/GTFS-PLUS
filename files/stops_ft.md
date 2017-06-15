## Additional Stops Information

 *  Filename MUST be `stops_ft.txt`
 *  File MUST contain a record for every transit stop or station (i.e. Embarcadero Station) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`stop_id`			| ID that uniquely identifies a stop

File MAY contain the following attributes:
 
Optional Attributes		| Description										
----------				| -------------		
`shelter`			    | String describing the shelter facility at the station. Valid entries include: 
`-` | `blank` - no information
`-` | `inside`
`-` | `sheltered`
`-` | `inside`
`-` | `none`
`lighting`			  | Boolean indicating presence of lighting.
`bike_parking`		| String describing bike parking facilities at station. Valid entires include:
`-` | `blank` - no information
`-` | `none`
`-` | `standard_outside`
`-` | `standard_inside`
`-` | `lockers`
`-` | `valet`
`bike_share_station`	 | Boolean indicating presence of a bike share station.
`seating`			      	 | Boolean. Indicates the presence of seating at the station. Stop-level overrides station-level.
`platform_height`		   | Float-point number in inches. Used with vehicle height to determine level boarding.
`level`				         | Integer, floors from street level.  Indicates how far up or below street level the stop is relative to the station and the station relative to the street level.
`off_board_payment`	   | Boolean indicating if there are fare gates or tagging stations before the platform.  Can be overriden by [`stop_times_ft`](stop_times_ft.md) value for a specific service.
`number_loading_areas` | Integer indicating the number of bus berths at the stop or station. This is a TCQSM parameter used to calculate dwell time.

