## Calendar
Filename: `calendar.txt`

 *  Filename MUST be `calendar.txt`
 *  File MUST contain a record for each service category used in [`trips.txt`](../trips.md)
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`service_id`		| ID that uniquely identifies the transit agency.
`start_date`		| Start date of service in YYYYMMDD format.  
`end_date`			| End date of service [ which is included in the service interval ] in YYYYMMDD format.  
`monday`			| 0 or 1. Binary value on whether this service pattern is available on Mondays.
`tuesday`			| 0 or 1. Binary value on whether this service pattern is available on Tuesdays.
`wednesday`			| 0 or 1. Binary value on whether this service pattern is available on Wednesdays.
`thursday`			| 0 or 1. Binary value on whether this service pattern is available on Thursdays.
`friday`			| 0 or 1. Binary value on whether this service pattern is available on Fridays.
`saturday`			| 0 or 1. Binary value on whether this service pattern is available on Saturdays.
`sunday`			| 0 or 1. Binary value on whether this service pattern is available on Sundays.
