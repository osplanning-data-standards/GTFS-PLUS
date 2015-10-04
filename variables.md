## Variables
This file describes some specific variables in more detail.

#### Mode <a name="mode">
The purpose of this field is to enable both transit sub-mode skimming and the assignment 
of various parameters on in vehicle time (i.e. making the perceived in vehicle time for 
commuter rail less than the perceived in vehicle time for a bus).  While the network mode 
values are flexible and adaptable to various agencies and situations, we have listed 
possible values to encourage inter-agency consistency.  The mode choice model specifies 
a set of network modes that can be used for each mode choice mode based on a modal 
hierarchy, defined in the Fast-Trips parameters files. Mode choice modes can either be 
general (i.e. walk-transit, which allows the use of all transit so long as it is accessed 
by walking) or specific (i.e. `walk-heavy_rail`, which might allow the use of local bus so 
long as it is used to access heavy rail).  Network mode definitions should have sufficient 
detail to be able to encapsulate the mode-choice mode definitions. 

 *  `local_bus`
 *  `premium_bus` (e.g., Community Transit, Sound Transit, Golden Gate Transit)
 *  `rapid_bus` (e.g., Van Ness BRT)
 *  `light_rail` (e.g., VTA Rail, Muni Metro, Link)
 *  `heavy_rail` (e.g., BART)
 *  `commuter_rail` (e.g., Sounder, Caltrain)
 *  `regional_rail` (e.g., SMART, eBART)
 *  `inter_regional_rail` (e.g., Amtrak, ACE, Capital Corridor)
 *  `high_speed_rail`
 *  `street_car` (i.e. F-line, SLU)
 *  `ferry`
 *  `cable_car`
 *  `open_shuttle` (i.e. Caltrain Shuttles, CPMC Shuttles)
 *  `employer_shuttle` (i.e. Microsoft, Google, and Facebook shuttles)
