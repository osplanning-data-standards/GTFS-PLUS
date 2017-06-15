## Additional Fare Attributes Information

Examples of how to specify various fare schemes can be found in the [fares page](../fares.md).

 *  Filename MUST be `fare_attributes_ft.txt`
 *  File MUST contain a record for each fare type.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.
 
 
Note: The one-to-one relationship between `route_id` and `fare_id` in [`fare_rules.txt`](../fares_rules.md) precludes 
the ability to represent fares that vary by time of day for the same route, 
e.g. peak/off-peak. Our work around is to use `fare_id`, `start_time` and `end_time` in 
[`fare_periods_ft.txt`](../fare_periods_ft.md) to return `fare_period`, which is then used in [`fare_attributes_ft.txt`](../fare_attributes_ft.md) 
to return the correct fare. 

Thus [`fare_attributes_ft.txt`](../fare_attributes_ft.md) substitutes (rather than augments) for [`fare_attributes.txt`](../fare_attributes.md).

File MUST contain the following attributes:

| Required Attributes	| Description										
| ----------			| -------------		
| `fare_period`		| Contains an ID that uniquely identifies the fare period.  The `fare_period` is dataset unique.
| `price`				| Float fare price in the unit specified by `currency_type`
| `currency_type`		| Defines the currency used to pay the fare in [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) alphabetical currency codes
| `payment_method`	| When the fare must be paid:
|					| 0 - on board
|					| 1 - before boarding
|`transfers`			| Number of transfers permitted on this fare:
|					| 0 - none
|					| 1 - one
|					| 2 - two  
|	    | (empty): If this field is empty, unlimited transfers are permitted  

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`transfer_duration`	| Integer length of time in seconds before transfer expires.  Omit or leave empty if they do not.

