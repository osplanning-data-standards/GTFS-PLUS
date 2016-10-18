## Additional Fare Rules

Adds a start and end time to fare rules.

Examples of how to specify various fare schemes can be found in the [fares page](../fares.md).

 *  Filename MUST be `fare_rules_ft.txt`
 *  File MUST contain a record for each fare rule start and end time.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`fare_id`			| An ID that links to `fare_id` in `fare_rules.txt`.  
`fare_class`		| Contains the name of the `fare_class` that links to the same attribute in `routes_ft.txt`. 
`start_time`		| (HH:MM:SS from midnight or blank/`default` to indicate a default fare)  This is so we can model fares that fluctuate by time of day. If no time of day is specified, it is assumed that this is the base fare and that other time of days will override it.
`end_time`			| (HH:MM:SS from midnight or blank/`default` to indicate a default fare)  Time when the fare is no longer valid (i.e. if the fare ends at 11:59:59, then `end_time` would be 12:00) This is so we can model fares that fluctuate by time of day. If no time of day is specified, it is assumed that this is the base fare and that other time of days will override it.

