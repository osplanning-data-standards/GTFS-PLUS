## Fare rules

Specifies how fares in the fare attributes file apply to an itinerary by O/D station, zones, or route.

Examples of how to specify various fare schemes can be found in the [fares page](../fares.md).

 *  Filename MUST be `fare_rules.txt`
 *  File MUST contain a record for each fare rule.
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

The combination of `route_id`, `origin_id`, and `destination_id` will be used to match a `fare_id` to a transit trip, in this order. The first match on this list will win.  
 1  Matching `route_id`, `origin_id` and `destination_id`  
 2  Matching `route_id` only (no `origin_id` or `destination_id` specified)  
 3  Matching `origin_id` and `destination_id` only (no `route_id` specified)  
 4  No match (e.g. `fare_id` specified with no other columns)  

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`fare_id`			| Unique identifier to fare class in fare attributes file

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`route_id`			| Associates a fare ID with a route ID from the routes file.  If multiple route have the same attributes, create a row for each route.
`origin_id`			| Origin fare zone ID, referenced from the stops file.  If several origin IDs have the same fare attributes, create a row for each origin ID.
`destination_id`	| Destination fare zone ID, referenced from the stops file.  If several fare destination IDs have the same fare attributes, create a row for each destination ID.
`contains_id`		| Associates a fare iD with a zone ID from the stops file and is associated with itineraries that pass through the `contains_id` zone.
