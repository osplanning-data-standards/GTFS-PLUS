## Additional Transit Route Information

 *  Filename MUST be `routes_stats_ft.txt`
 *  File MUST contain a record for every transit route (i.e. the Muni 14 Local) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain ONE the following TWO sets of required attributes:

**Option One**:

Required Attributes	| Description										
----------			| -------------		
`route_id`			| ID that uniquely identifies a route.
`start_date`		| Start date in YYYYMMDD for which route statistics are calculated.
`end_date`			| End date in YYYYMMDD for which route statistics are calculated.
`start_time`		| Start time in HH:MM:SS for which route statistics are calculated.
`end_time`			| End time in HH:MM:SS for which route statistics are calculated.
`monday`			| 0 or 1. A binary value indicating whether route statistics include Mondays.
`tuesday`			| 0 or 1. A binary value indicating whether route statistics include Tuesdays.
`wednesday`			| 0 or 1. A binary value indicating whether route statistics include Wednesdays.
`thursday`			| 0 or 1. A binary value indicating whether route statistics include Thursdays.
`friday`			| 0 or 1. A binary value indicating whether route statistics include Fridays.
`saturday`			| 0 or 1. A binary value indicating whether route statistics include Saturdays.
`sunday`			| 0 or 1. A binary value indicating whether route statistics include Sundays.

**Option Two**:

Required Attributes	| Description										
----------			| -------------		
`service_id`		| ID that uniquely identifies a service span in `calendar.txt`.
`start_time`		| Start time in HH:MM:SS for which route statistics are calculated.
`end_time`			| End time in HH:MM:SS for which route statistics are calculated.

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`schedule_time`		| Integer, mean number of minutes from scheduled `arrival_time` at first stop to scheduled `departure_time` at last stop.
`actual_time`		| Integer, mean number of minutes from actual `arrival_time` at first stop to actual `departure_time` at last stop.
`std_dev`			| Float, standard deviation of `actual_time`.
`semi_std_dev`		| Float, semi-standard deviation between scheduled and actual route run time.
`schedule_stop_time`| Integer, mean number of minutes scheduled stop time.
`actual_stop_time`	| Integer, mean number of minutes actual stop time.
`stop_delay`		| Integer, mean number of minutes of stop delay.
`schedule_move_time`| Integer, mean number of minutes scheduled moving time.
`actual_move_time`	| Integer, mean number of minutes actual moving time.
`move_delay`		| Integer, mean number of minutes of moving delay.
