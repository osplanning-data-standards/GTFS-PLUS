## Additional Transit Route Information

 *  Filename MUST be `routes_ft.txt`
 *  File MUST contain a record for every transit route (i.e. the Muni 14 Local) 
 *  File MUST be a valid CSV file.
 *  The first line of each file MUST contain case-sensitive field names.
 *  Field names MUST NOT contain tabs, carriage returns or new lines.

File MUST contain the following attributes:

Required Attributes	| Description										
----------			| -------------		
`route_id`			| ID that uniquely identifies a route
[`mode`](../variables.md#mode)			| The mode field is used to specify the network mode of the route. Valid entries include:
`-` | `local_bus`
`-` | `premium_bus` such as Golden Gate Transit, Community Transit
`-` | `rapid_bus` such as VanNess BRT
`-` | `light_rail` such as LINK, Muni Metro, and VTA Rail
`-` | `heavy_rail` such as BART
`-` | `commuter_rail` such as Sounder and Caltrain
`-` | `inter_regional_rail` such as Amtrak, and ACE
`-` | `high_speed_rail`
`-` | `street_car` such as Muni F-Line or the SLUT
`-` | `ferry`
`-` | `cable_car`
`-` | `open_shuttle` such as Caltrain or CPMC Shuttles
`-` | `employer_shuttle` such as Google, Microsoft and Facebook

File MAY contain the following attributes:

Optional Attributes	| Description										
----------			| -------------		
`proof_of_payment`	| A boolean value indicating if the route has fare enforcement through random inspection (true) or if the driver oversees payment (false). 
`percent_using_farebox` | Floating point value between 0 and 1 indicating the percent of passengers boarding who pay a cash fare at the farebox (as opposed to paying via Smart Card or other payment method. This value will be overridden by `percent_using_farebox` in `stop_times_ft`, if provided.
