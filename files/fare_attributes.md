## Fare Attributes

Examples of how to specify various fare schemes can be found in the [fares page](../fares.md).

 *  Filename MUST be `fare_attributes.txt`
 *  File MUST contain a record for each fare type.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`fare_id`			| Contains an ID that uniquely identifies the fare class.  The `fare_id` is dataset unique.
`price`				| Float fare price in the unit specified by `currency_type`
`currency_type`		| Defines the currency used to pay the fare in [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) alphabetical currency codes
`payment_method`	| When the fare must be paid:
-					| 0 - on board
-					| 1 - before boarding
`transfers`			| Number of transfers permitted on this fare:
-					| 0 - none
-					| 1 - one
-					| 2 - two  
-				    | (empty): If this field is empty, unlimited transfers are permitted   

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`transfer_duration`	| Integer length of time in seconds before transfer expires.  Omit or leave empty if they do not.

