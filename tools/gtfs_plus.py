"""
This file contains helper scripts to create GTFS Plus files from GTFS files.
"""

__copyright__ = "Copyright 2017 Contributing Entities"
__license__   = """
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import csv
import transitfeed
import pandas as pd

def routesft_assume_mode(schedule, default_mode):
    routeid_to_mode_dict = dict(zip(schedule.routes.keys(),[default_mode]*len(schedule.routes.keys())))
    return routeid_to_mode_dict


def get_transfer_dist(schedule):
    for k,v in schedule._transfers.iteritems():
        from_stop_id,to_stop_id = k
        
        from_lat = schedule.stops[from_stop_id].stop_lat
        from_lon = schedule.stops[from_stop_id].stop_lon
        to_lat   = schedule.stops[to_stop_id].stop_lat
        to_lon   = schedule.stops[to_stop_id].stop_lon
        

def haversine((lat1, lon1), (lat2, lon2)):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    returns miles
    """
    from math import radians, cos, sin, asin, sqrt
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    miles = 0.621371 * km
    return miles 

def create_tranfers(schedule,max_xfer_dist = 0.5):
    from itertools import combinations
    5 #miles
    
    #create pairwise iterator
    stops = {}
    for key,val in schedule.stops.iteritems():
        stops[key]=(val.stop_lat, val.stop_lon)
    
    pair = list(set(list(combinations(stops, r=2))))
    #print "PAIR",pair
    
    #get xfer distance between each combination
    #potential_xfer_dict = {(pair[0][0],pair[1][0]): haversine(pair[0][1],pair[1][1]) }
    
    potential_xfer_dict = {p:haversine(stops[p[0]],stops[p[1]]) for p in pair }
    
    #delete pairs that are greater than maximum xfer distance
    del_keys = []
    for k,v in potential_xfer_dict.iteritems():
        if v > max_xfer_dist:
            del_keys.append(k)
    for k in del_keys:
        del potential_xfer_dict[k]
        
    #return dictionary with valid values
    return potential_xfer_dict
    
    