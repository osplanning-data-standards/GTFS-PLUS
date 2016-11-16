## Transfer Links
Filename: `transfers.txt`

 *  Filename MUST be `transfers.txt`
 *  File MUST contain a record for each pair of transit stops that can be transferred between 
 on foot.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:
 
Required Attributes	| Description										
----------			| -------------		
`from_stop_id`		| From `stop_id` or park and ride / kiss and ride node.  Cannot be the same as `to_stop_id`.
`to_stop_id`		| To `stop_id` or park and ride / kiss and ride node. Cannot be the same as `from_stop_id`.
`transfer_type`		| Type of transfer:
-					| 0 / Empty - a recommended transfer point
-					| 1 - timed transfer between two routes
-					| 2 - requires a minimum amount of time, specified by `min_transfer_time`
-					| 3 - transfers not possible between routes
`min_transfer_time`	| When a connection between routes requires an amount of time between arrival and departure (`transfer_type`=2), this field defines the amount of time that must be available for a typical rider - in seconds.

