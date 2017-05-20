## Fares
Fares can be quite complex.  This page illustrates examples of how to specify them.

### Single leg, no transfer, flat fare

The example below illustrates how the fare for a single leg transit trip using a service 
that has flat fare system. First [`fare_rules.txt`](../fare_rules.md) is queried on `route_id`, `origin_zone` & 
`destination_zone` to return it’s `fare_id`.  In this case, origin and destination zones have a value of None, 
which represents cases where stops are never used in a zonal fee 
structure. Then, [`fare_periods_ft.txt`](../fare_periods_ft.md) is queried on `fare_id` and the time of departure (>= to 
`start_time`, <= `end_time`) to return `fare_period`. Finally, [`fare_attributes_ft.txt`](../fare_attributes_ft.md) is queried 
on `fare_period`, and the cost of the fare is returned by the `price` field. 

*[`stops.txt`](/files/stops.md)*

`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
--------- 	| -----	 		| -----	   	| -----	
1 			| 14th/Mission 	| - 		| ...
2 			| 30th/Mission 	| - 		| ...

*[`fare_rules.txt`](/files/fare_rules.md)*

`fare_id` 		| `route_id`
--------- 		| -----
muni-local	| MUN14

*[`fare_periods_ft.txt`](/files/fare_periods_ft.md)*

`fare_id` 		| `fare_period` 	| `start_time`	| `end_time`											
--------- 		| -----	 		| -----	  		| ---- 		
muni-local		| muni-allday 	| 00:00:00 		| 24:00:00 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*

`fare_period`	| `price` 	| `currency_type`	| `transfers`	| `transfer_duration`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
muni-allday		| 2.50 		| USD 				| -				| 5400

### Two or more legs, transfer

To capture the cost of this scenario, the cost of each leg is calculated using the same 
method proposed for a single leg trip. We then use the *from* `fare_period` and the *to* 
`fare_period` to get the `transfer_fare_type`, which has three possible values: `transfer_cost`, `transfer_discount`, or `transfer_free`. The transfer is free if the value of this field is `transfer_free`. If `transfer_discount`, the amount in the `transfer_fare` field is subtracted from the the full cost of the fare of the to leg. If `transfer_cost`, the full amount of the `transfer_fare` field is the cost of the transfer.

### Multiple Transfers
A second transfer would work in a similar fashion, however, it is possible (unlikely ?) that the fare would have to be calculated using the *from* `fare_period` for both the first and second leg to determine which `transfer_rule` to use. For example, a rider uses the same `fare_period` in the first and third leg of a three leg trip. This `fare_period` is entitled to a free transfer (`transfer_fare_type` = `transfer_free`) when staying with the same fare_period during a transfer (e.g. a metro bus to metro bus transfer). Assuming the transfer has not expired (and this scenario is permitted), the rider is eligible for a free transfer based on the `fare_period` associated with the first leg of the trip, even if there is a transfer cost associated with the second and third leg.  

### Systemwide Fare
The following two-leg (one transfer) trip demonstrates how a system-wide fare would be 
calculated using Pierce Transit as an example. First, [`fare_rules.txt`](../fare_rules.md) is queried on the 
`route_id`, `origin_zone` and `destination_zone` of the first leg to return its `fare_id`.  In 
this case, the origin and destination have zones but are the same because these stops need 
zones for Sound Transit, our regional express bus service. Then [`fare_periods_ft.txt`](../fare_periods_ft.md) is 
queried on `fare_id` and the time of departure (>= to `start_time`, <= `end_time`) to return 
`fare_period`. Next, [`fare_attributes_ft.txt`](../fare_attributes_ft.md) is queried on `fare_period`, and the cost of the fare 
is returned by the `price` field. 

The next step is to determine the transfer rule for this particular transfer. We use the 
`route_id` of the second leg to get the `fare_id` which, along with departure time, is used 
to get `fare_period` from [`fare_periods_ft.txt`](../fare_periods_ft.md). The `from_fare_period`  and the `to_fare_period` are used 
to get `tranfer_fare_type` and `transfer_far` from [`fare_transfer_rules_ft.txt`](../fare_transfer_rules_ft.md). In this case `transfer_fare_type` is `transfer_free` indicating that there is no fee for the second leg of this trip. 

**First Leg:**

*[`stops.txt`](/`file`s/stops.md)*

`stop_id` 	| `stop_name` 				| `zone_id`	| ...										
--------- 	| -----	 					| -----	   	| -----	
1 			| Pacific Ave/166th St. 	| Tacoma	| ...
2 			| Pacific Ave/112th St. 	| Seattle	| ...

*[`routes_ft.txt`](/files/routes_ft.md)*

`route_id`	| `mode` 		| `proof_of_payment`										
----------	| -----	 		| -----	
PT01  		| `local_bus` | 1

*[`fare_rules.txt`](/files/fare_rules.md)*

`fare_id` 		| `route_id`	| `origin_id`	| `destination_id`										
--------- 		| -----	 		| -----	   		| -----
Pierce-Local	| PT01			| Pierce		| Pierce

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*

`fare_id` 		| `fare_period` 		| `start_time`	| `end_time`											
--------- 		| -----	 			| -----	  		| ---- 		
Pierce-Local	| Pierce-AllDay 	| 00:00:00 		| 24:00:00 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*

`fare_period`	| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
Pierce-AllDay	| 2.00 		| USD 				| -				| 1

**Second Leg:**

*[`stops.txt`](/files/stops.md)*

`stop_id` 	| `stop_name` 				| `zone_id`	| ...										
--------- 	| -----	 					| -----	   	| -----	
3 			| Pacific Ave/112th St. 	| Pierce	| ...
4 			| SR 512 PNR			 	| Pierce	| ...

*[`routes_ft.txt`](/files/routes_ft.md)*

`route_id`	| `mode` 		| `proof_of_payment`										
----------	| -----	 		| -----	
PT53  		| local_bus 	| 1

*[`fare_rules.txt`](/files/fare_rules.md)*

`fare_id` 		| `route_id`	| ...										
--------- 		| -----	 		| -----	   		
Pierce-Local	| `PT53`		| ...

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*

`fare_id` 		| `fare_period` 		| `start_time`	| `end_time`											
--------- 		| -----	 			| -----	  		| ---- 		
Pierce-Local	| Pierce-AllDay 	| 00:00:00 		| 24:00:00 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*

`fare_period`	| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
Pierce-AllDay	| 2.00 		| USD 				| -				| 1

*[`fare_transfer_rules_ft.txt`](/files/fare_transfer_rules_ft.md)*

`from_fare_period` 	| `to_fare_period` 	| `transfer_fare_type`| `transfer_fare`											
--------- 			| -----	 			| -----	  		| ---- 		
Pierce-AllDay		| Pierce-AllDay 	| `transfer_free`			| 0	

### Inter-Agency Fare, zonal fee structure
The following illustrates how an inter-agency fare (one transfer, two different fare classes) would be calculated. First, [`fare_rules.txt`](../fare_rules.md) is queried on the `route_id`, `origin_zone` and `destination zone` of the first leg to return its `fare_id`. Then [`fare_periods_ft.txt`](../fare_periods_ft.md) is queried on `fare_id` and the time of departure (>= to `start_time`, <= `end_time`) to return `fare_period`. Next, [`fare_attributes_ft.txt`](../fare_attributes_ft.md) is queried on `fare_period`, and the cost of the fare is returned by the `price` field.

The next step is to determine the transfer rule for this particular transfer. We use the `route_id` of the second leg to get the `fare_id` which can then be used to get `fare_period`. We then get the rule that applies to this transfer, which is returned by querying [`fare_transfer_rules_ft.txt`](../fare_transfer_rules_ft.md) on `from_fare_period` and `to_fare_period`. In this case, the field `transfer_fare_type` in the returned record is `transfer_cost`, indicating the amount in the `transfer_fare` field is the cost of the transfer.

**First Leg:**

*[`stops.txt`](../stops.md)* 

`stop_id` | `stop_name` | `zone_id` | ...
----- | -----	| -----	| -----	
1 | TACOMA_DOME | Tacoma | ...
2 | 4th Ave & Cherry | Seattle | ...

*[`fare_rules.txt`](../fare_rules.md)*

`fare_id` | `origin_id` | `contains_id`
----- 	| -----	| -----	
ST_EXPRESS  | Tacoma | 0

*[`fare_periods_ft.txt`](../fare_periods_ft.md)*

`fare_id` | `fare_period` | `start_time` | `end_time` 
----- | -----	| -----	| -----	
ST_EXPRESS | ST_EXPRESS_2Z | 00:00:00 | 24:00:00

*[`fare_attributes_ft.txt`](../fare_attributes_ft.md)* 

`fare_period` | `price` | `currency_type` | `payment_method` | `transfers`
----- | -----	| -----	| -----	| -----	
ST_EXPRESS_2Z | 3.40 | USD | 1 | 2

**Second leg:**

*[`stops.txt`](../stops.md)*

`stop_id` | `stop_name` | `zone_id` | ...
----- | -----	| -----	| -----	
3 | James St. & 3rd Ave. | Seattle | ...
4 | E Jefferson St & 17th Ave | Seattle | ...

*[`fare_rules.txt`](../fare_rules.md)* 

`fare_id` | `origin_id` | `destination_id`
----- 	| -----	| -----	
Metro_1Z | Seattle | Seattle

*[`fare_periods_ft.txt`](../fare_periods_ft.md)*

`fare_id` | `fare_period` | `start_time` | `end_time`
----- | -----	| -----	| -----	
Metro_1Z | METRO_1Z_P | 06:00:00 | 09:00:00

*[`fare_attributes_ft.txt`](../fare_attributes_ft.md)*

`fare_period` | `price` | `currency_type` | `payment_method` | `transfers`
----- | -----	| -----	| -----	| -----	
Metro_1Z_P | 2.75 | USD | 1 | -

*[`fare_transfer_rules_ft.txt`](../fare_transfer_rules_ft.md)*

`from_fare_period` | `to_fare_period` | `transfer_fare_type` | `transfer_fare`
----- | -----	| -----	| -----	
ST_EXPRESS_2Z | Metro_1Z_P | False | 1

### Zone-Based Fares
Commuter rail frequently calculates fares based on the number of zones you traverse.  This 
can be specified as follows.

*[`stops.txt`](/files/stops.md)*

`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
----- 	| -----	 		| -----	   	| -----	
1 			| PIONEER_SQ 	| Seattle	| ...
2			| EVERETT		| Everett	| ...

*[`fare_rules.txt`](/files/fare_rules.md)*

`fare_id` 		| `origin_id`	| `destination_id`										
------ 		| -----	 		| -----	   		
SOUNDER-2Z	| Seattle		| Everett

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*

`fare_id` 	| `fare_period` 		| `start_time`	| `end_time`											
--------- 	| -----	 			| -----	  		| ---- 		
SOUNDER-2Z	| Sounder-2Z-AllDay | 00:00:00 		| 24:00:00 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*

`fare_period`		| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 			| -----	 	| -----	 			| -----			| -----  		
Sounder-2Z-AllDay	| 2.00 		| USD 				| -				| 1

### OD-Based Fares
Origin-destination based fares are common on heavy rail systems, such as BART.  They are 
a special case of zone-based fares, where every station has its own zone, and could be 
specified as follows.

*[`stops.txt`](/files/stops.md)*

`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
--------- 	| -----	 		| -----	   	| -----	
1 			| EMBARCADERO 	| B-EMB		| ...
2			| FREMONT		| B-FRE		| ...

*[`fare_rules.txt`](/files/fare_rules.md)*

`fare_id` 	| `origin_id`	| `destination_id`										
--------- 	| -----	 		| -----	   		
B-EMB-FRE	| B-EMB		| B-FRE

*[`fare_periods_ft.txt`](/files/fare_periods_ft.md)*

`fare_id` 	| `fare_period` 		| `start_time`	| `end_time`											
--------- 	| -----	 			| -----	  		| ---- 		
B-EMB-FRE	| B-EMB-FRE-AllDay	| 00:00:00 		| 24:00:00 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*

`fare_period`		| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 			| -----	 	| -----	 			| -----			| -----  		
B-EMB-FRE-AllDay	| 2.75 		| USD 				| -				| 1
