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
`from_fare_period`	| An ID that identifies the `fare_period` that the passenger is coming from.  
`to_fare_period`	| An ID that identifies the `fare_period' that the passenger is going to.  
`transfer_fare_type` |   One of:
 `-` | `transfer_cost`:  assumes that the full value fare is not paid again  
 `-` | `transfer_discount`:   is a subtraction from the cumulative fare  
 `-` | `transfer_free`:  is a ridiculous way to say "free transfer"  
`transfer_fare`		|  If `transfer_fare_type` `==` `transfer_free`, this column is ignored.  Otherwise, this must be a non-negative value in whatever the fare currency that is added to the initial fare in the case of a transfer cost or subtracted from the combined fare of the segments in the case of transfer discount.

