
## GTFS-Plus

A GTFS-based data transit network data standard suitable for dynamic transit modeling.

**version**: 0.2.0  
**updated**: 18 September 2015  
**created**: 09 July 2015  
**authors**:  

 * Stefan Coe (Puget Sound Regional Council)  
 * Elizabeth Sall (UrbanLabs LLC)  
 * Lisa Zorn (LMZ LLC)  
 * Drew Cooper (San Francisco County Transportation Authority)  
 
[issues]: https://github.com/osplanning-data-standards/GTFS-PLUS/issues
[repo]: https://github.com/osplanning-data-standards/GTFS-PLUS
[GTFS]: https://developers.google.com/transit/gtfs/reference


NOTE: This is a draft specification and still under development. If you have comments
or suggestions please file them in the [issue tracker][issues]. If you have
explicit changes please fork the [git repo][repo] and submit a pull request.

### Changelog

-  `0.1.0`: initial commit; [Technical Memo Documentation](http://fast-trips.mtc.ca.gov/library/T2-NetworkDesign-WorkingCopy-July2015V0.1.pdf)  
-  `0.2.0`: added additional required fields to [`transfers_ft.txt`](/files/transfers_ft.md) 
in order to support route-specific transfers and time-point precedence. [Technical Memo Documentation](http://fast-trips.mtc.ca.gov/library/T2-NetworkDesign-StaticCopy-Sept2015V0.2.pdf)  

# Specification

A GTFS-PLUS transit network consists of required and optional data files that together 
describe a network of transit service.  Files not denoted with `_ft` follow the same format 
as the General Transit Feed Specification - [GTFS].

A GTFS-PLUS transit network MUST include the following files:

Filename 			| Description										
----------			| -------------										
[`walk_access.txt`](/files/walk_access.md)	| walk access links									
[`transfers.txt`](/files/transfers.md)		| transfer links									
[`trips.txt`](/files/trips.md)				| transit vehicle trips								
[`trips_ft.txt`](/files/trips_ft.md)		| additional transit vehicle trip information		
[`routes.txt`](/files/routes.md)			| transit routes									
[`routes_ft.txt`](/files/routes_ft.md)		| additional transit route information				
[`stops.txt`](/files/stops.md)				| transit stops and stations						
[`stops_ft.txt`](/files/stops_ft.md)		| additional transit stop and station information	
[`stop_times.txt`](/files/stop_times.md)	| transit trip stop times							
[`stop_times_ft.txt`](/files/stop_times.md)	| additional transit trip stop time information		
[`vehicles_ft.txt`](/files/vehicles_ft.md)	| transit vehicles									
[`agency.txt`](/files/agency.md)			| transit agency									
[`calendar.txt`](/files/calendar.md)		| transit schedule calendar							

A GTFS-PLUS transit network MAY include the following files:

Filename 					| Description										
----------					| -------------		
[`transfers_ft.txt`](/files/transfers_ft.md)		| additional transit link information
[`drive_access.txt`](/files/drive_access.md)		| drive access links
[`pnr.txt`](/files/pnr.md)							| park and ride access links
[`knr.txt`](/files/knr.md)							| kiss and ride access links
[`shapes.txt`](/files/shapes.md)					| transit route shape points
[`fare_attributes.txt`](/files/fare_attributes.md)			| fare attributes
[`fare_rules.txt`](/files/fare_rules.md)					| fare rules
[`fare_rules_ft.txt`](/files/fare_rules_ft.md)				| additional fare rules
[`fare_transfer_rules.txt`](/files/fare_transfer_rules.md)	| fare transfer rules

# Fares

Examples of how to specify various fare schemes can be found in the [fares page](fares.md).













