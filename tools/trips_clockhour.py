# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:45:42 2017

@author: jchang

This code adds clock hour equivalents of post-midnight trips (trips whose first stop time >= 24:00:00);
Four files are modified: stops_times.txt, stop_times_ft.txt, trips.txt, trips_ft.txt

"""

import numpy as np
import pandas as pd
import sys,os

input_dir = r'Q:\Model Development\SHRP2-fasttrips\Task2\built_fasttrips_network_2012Base\draft1.14_fare'
output_dir = r'Q:\Model Development\SHRP2-fasttrips\Task2\built_fasttrips_network_2012Base\draft1.14_fare_clockhour'

st = pd.read_csv(os.path.join(input_dir,'stop_times.txt'))
stf = pd.read_csv(os.path.join(input_dir,'stop_times_ft.txt'))
tp = pd.read_csv(os.path.join(input_dir,'trips.txt'))
tpf = pd.read_csv(os.path.join(input_dir,'trips_ft.txt'))

a,b,c = st['arrival_time'].str.split(':').str
a=a.astype(int)

trip_ids = st[(a>=24) & (st['stop_sequence']==1)]['trip_id']

st_add = st[st['trip_id'].isin(trip_ids)]
st_add['trip_id']=st_add['trip_id']+max(st['trip_id'])
tp_add = tp[tp['trip_id'].isin(trip_ids)]
tp_add['trip_id'] = tp_add['trip_id']+max(st['trip_id'])
tp_final = tp.append(tp_add)
tpf_add = tpf[tpf['trip_id'].isin(trip_ids)]
tpf_add['trip_id']=tpf_add['trip_id']+max(st['trip_id'])
tpf_final = tpf.append(tpf_add)

def restore_clock_hour(timestring):
    h,m,s = timestring.split(':')
    h=int(h)-24
    return '0%s:%s:%s' %(h,m,s)
st_add['arrival_time']=st_add['arrival_time'].apply(restore_clock_hour)
st_add['departure_time']=st_add['departure_time'].apply(restore_clock_hour)

st_final = st.append(st_add)

stf_final = st_final[['trip_id','stop_id']]

st_final.to_csv(os.path.join(output_dir,'stop_times.txt'),index=False)
stf_final.to_csv(os.path.join(output_dir,'stop_times_ft.txt'),index=False)
tp_final.to_csv(os.path.join(output_dir,'trips.txt'),index=False)
tpf_final.to_csv(os.path.join(output_dir,'trips_ft.txt'),index=False)
