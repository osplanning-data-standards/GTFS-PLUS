## Fare Transfer Rules

Examples of how to specify various fare schemes can be found in the [fares page](../fares.md).

 *  Filename MUST be `fare_transfer_rules_ft.txt`
 *  File MUST contain a record for each transfer rule for fares.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`from_fare_class`	| An ID that identifies the `fare_class` that the passenger is coming from.  
`to_fare_class`		| An ID that identifies the `fare_class` that the passenger is going to.  
`is_flat_fee`		| A boolean flag that indicates if a flat fare is paid or the fare is a percentage of the full fare for that leg. If True, a flat fee is expected in the `tranfer_rule` field, e.g. 1.50. Otherwise the value in `tranfer_rule` should range from 0-1. 
`transfer_rule`		| If `is_flat_fee` is true, value should be a monetary amount, e.g 1.50. Otherwise, this field contains the amount, from 0-1, that will be multiplied to the fare of the transfer leg to return the amount of the transfer. 

