## Additional Stop Time Information

 *  Filename MUST be `stop_times_ft.txt`
 *  File MUST contain a record for every scheduled stop within a trip and route (i.e. the time when the Muni 14 Local Outbound that left at 8:02 gets to 24th St. and Mission St)
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`trip_id`			| ID that uniquely identifies trip
`stop_id`			| ID that uniquely identifies a stop

File MAY contain the following attributes:

Optional Attributes		| Description										
----------				| -------------		
`pay_at_station`		| Boolean indicating if the passenger can pay at the stop
`real_time_data`		| Boolean indicating the presences of real time data displayed while waiting.  Stop level overrides station level.
`front_board_only`		| Boolean indicating the boarding can only be made through the front doors. 
`reliability`			| Not yet defined.
`level_boarding`		| Boolean indicating the level_boarding field indicates if the platform and the bus are level. Overrides logic from platform height.
`percent_using_farebox` | Floating point value between 0 and 1 indicating the percent of passengers boarding who pay a cash fare at the farebox (as opposed to paying via Smart Card or other payment method. This value will be override `percent_using_farebox` in `routes_ft`.
