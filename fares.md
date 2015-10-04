##Fares

Fares can be quite complex.  This page illustrates examples of how to specify them.

#### Single leg, no transfer, flat fare

The example below illustrates how the fare for a single leg transit trip using a service 
that has flat fare system. First `fare_rules.txt` is queried on `route_id`, `origin_zone` & 
`destination_zone` to return it’s `fare_id`.  In this case, Origin and destination zones 
have values of None, which represent cases where stops are never used in a zonal fee 
structure. `Fare_rules_ft.txt` is then queried on `fare_id` and the time of departure (>= to 
`start_time`, <= `end_time`) to return `fare_class`. `Fare_attributes_ft.txt` is then queried 
on `fare_class`, and the cost of the fare is returned by the price field. 

*[`stops.txt`](/files/stops.md)*
`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
--------- 	| -----	 		| -----	   	| -----	
1 			| 14th/Mission 	| - 		| ...
1 			| 30th/Mission 	| - 		| ...

*[`routes_ft.txt`](/files/routes_ft.md)*
`route_id`	| `mode` 		| `fare_class` 	| `proof_of_payment`										
----------	| -----	 		| -----	    	| -----	
MUN14  		| `local_bus` 	| muni-local 	| 1
MUN14R 		| `rapid_bus` 	| muni-local 	| 1

*[`fare_rules.txt`](/files/fare_rules.md)*
`fare_id` 		| `route_id` 	| `contains_id`											
--------- 		| -----	 		| -----	   		
muni-allday	| muni-local 	| - 			

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*
`fare_id` 		| `fare_class` 	| `start_time`	| `end_time`											
--------- 		| -----	 		| -----	  		| ---- 		
muni-allday		| muni-local 	| 000001 		| 240000 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*
`fare_class`	| `price` 	| `currency_type`	| `transfers`	| `transfer_duration`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
muni-local		| 2.50 		| USD 				| -				| 5400

#### Two or more legs, transfer

To capture the cost of this scenario, the cost of each leg is calculated using the same 
method proposed for a single leg trip. We then use the from `fare_class` and the to 
`fare_class` to get the `is_flat_fee` and `transfer_rule` attributes from 
`fare_transfer_rules.txt`. `is_flat_fee` is a boolean that indicates if the transfer is
percentage- or flat-fee based. For example, if `is_flat_fee` is True, the fare for the 
second leg of the trip is the amount in `tranfer_rule` (e.g., 1.50). To indicate a free 
transfer, `reduced_rate `is set to True and `tranfer_rule` is set to 0.

#### Systemwide Fare
The following two-leg (one transfer) trip demonstrates how a system-wide fare would be 
calculated using Pierce Transit as an example. First, `fare_rules.txt` is queried on the 
`route_id`, `origin_zone` and `destination_zone` of the first leg to return it’s `fare_id`.  In 
this case, Origin and destination have zones but are the same because these stops need 
zones for Sound Transit, our regional express bus service. `Fare_rules_ft.txt` is then 
queried on `fare_id` and the time of departure (>= to `start_time`, <= `end_time`) to return 
`fare_class`. `Fare_attributes_ft.txt` is then queried on `fare_class`, and the cost of the fare 
is returned by the `price` field. 

The next step is to determine the transfer rule for this particular transfer. We use the 
`route_id` of the second leg to get the `fare_id` which, along with departure time, is used 
to get `fare_class` from `fare_rules_ft.txt`. The `from_fare_class`  and the `to_fare_class` are used 
to get `reduced_rate` and `transfer_cost` from `fare_transfer_rules.txt`. In this case 
`reduced_rate` is True the and `fare_cost` is 0 indicating that there is no fee for the second 
leg of this trip. 

*First Leg*

*[`stops.txt`](/files/stops.md)*
`stop_id` 	| `stop_name` 				| `zone_id`	| ...										
--------- 	| -----	 					| -----	   	| -----	
1 			| Pacific Ave/166th St. 	| Tacoma	| ...
2 			| Pacific Ave/112th St. 	| Seattle	| ...

*[`routes_ft.txt`](/files/routes_ft.md)*
`route_id`	| `mode` 		| `fare_class` 	| `proof_of_payment`										
----------	| -----	 		| -----	    	| -----	
PT01  		| `local_bus` 	| Pierce 		| 1

*[`fare_rules.txt`](/files/fare_rules.md)*
`fare_id` 		| `route_id`	| `origin_id`	| `destination_id`										
--------- 		| -----	 		| -----	   		| -----
Pierce-Local	| PT0`			| Pierce		| Pierce

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*
`fare_id` 		| `fare_class` 		| `start_time`	| `end_time`											
--------- 		| -----	 			| -----	  		| ---- 		
Pierce-Local	| Pierce-AllDay 	| 000001 		| 240000 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*
`fare_class`	| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
Pierce-Allday	| 2.00 		| USD 				| -				| 1

*Second Leg*

*[`stops.txt`](/files/stops.md)*
`stop_id` 	| `stop_name` 				| `zone_id`	| ...										
--------- 	| -----	 					| -----	   	| -----	
3 			| Pacific Ave/112th St. 	| Pierce	| ...
4 			| SR 512 PNR			 	| Pierce	| ...

*[`routes_ft.txt`](/files/routes_ft.md)*
`route_id`	| `mode` 		| `fare_class` 	| `proof_of_payment`										
----------	| -----	 		| -----	    	| -----	
PT53  		| local_bus 	| Pierce		| 1

*[`fare_rules.txt`](/files/fare_rules.md)*
`fare_id` 		| `route_id`	| ...										
--------- 		| -----	 		| -----	   		
Pierce-Local	| `PT04`		| ...

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*
`fare_id` 		| `fare_class` 		| `start_time`	| `end_time`											
--------- 		| -----	 			| -----	  		| ---- 		
Pierce-Local	| Pierce-AllDay 	| 000001 		| 240000 	

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*
`fare_class`	| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 		| -----	 	| -----	 			| -----			| -----  		
Pierce-Allday	| 2.00 		| USD 				| -				| 1

*[`fare_transfer_rules.txt`](/files/fare_transfer_rules.md)*
`from_fare_class` 	| `to_fare_class` 	| `sis_flat_fee`| `transfer_rule`											
--------- 			| -----	 			| -----	  		| ---- 		
Pierce-AllDay		| Pierce-AllDay 	| False			| 0	

#### Zone-Based Fares
Commuter rail frequently calculates fares based on the number of zones you traverse.  This 
can be specified as follows.

*[`stops.txt`](/files/stops.md)*
`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
--------- 	| -----	 		| -----	   	| -----	
1 			| PIONEER_SQ 	| Seattle	| ...
2			| EVERETT		| Everett	| ...

*[`fare_rules.txt`](/files/fare_rules.md)*
`fare_id` 		| `origin_id`	| `destination_id`										
--------- 		| -----	 		| -----	   		
SOUNDER-2Z	| Seattle		| Everett

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*
`fare_id` 	| `fare_class` 		| `start_time`	| `end_time`											
--------- 	| -----	 			| -----	  		| ---- 		
SOUNDER-2Z	| Sounder-2Z-AllDay | 000001 		| 240000 	


*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*
`fare_class`		| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 			| -----	 	| -----	 			| -----			| -----  		
Sounder-2Z-AllDay	| 2.00 		| USD 				| -				| 1

#### Zone-Based Fares; Peak Fares
Origin-destination based fares are common on heavy rail systems, such as BART.  They are 
a special case of zone-based fares, where every station has its own zone, and could be 
specified as follows.  This example also shows the use of peak fares.

*[`stops.txt`](/files/stops.md)*
`stop_id` 	| `stop_name` 	| `zone_id`	| ...										
--------- 	| -----	 		| -----	   	| -----	
1 			| EMBARCADERO 	| B-EMB		| ...
2			| FREMONT		| B-FRE		| ...

*[`fare_rules.txt`](/files/fare_rules.md)*
`fare_id` 	| `origin_id`	| `destination_id`										
--------- 	| -----	 		| -----	   		
B-EMB-FRE	| B-EMB		| B-FRE

*[`fare_rules_ft.txt`](/files/fare_rules_ft.md)*
`fare_id` 	| `fare_class` 		| `start_time`	| `end_time`											
--------- 	| -----	 			| -----	  		| ---- 		
B-EMB-FRE	| B-EMB-FRE-AllDay	| 000001 		| 240000 	
B-EMB-FRE	| B-EMB-FRE-AMPeak	| 070000 		| 083000 	
B-EMB-FRE	| B-EMB-FRE-PMPeak	| 170000 		| 183000 

*[`fare_attributes_ft.txt`](/files/fare_attributes_ft.md)*
`fare_class`		| `price` 	| `currency_type`	| `transfers`	| `payment_method`											
--------- 			| -----	 	| -----	 			| -----			| -----  		
B-EMB-FRE-AllDay	| 2.75 		| USD 				| -				| 1
B-EMB-FRE-AMPeak	| 4.75 		| USD 				| -				| 1
B-EMB-FRE-PMPeak	| 4.75 		| USD 				| -				| 1
