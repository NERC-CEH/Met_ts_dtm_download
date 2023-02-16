#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script that attributes a 2016 CSS file with met office data.

@author: Ciaran Robb
"""

import os 
from eot.downloader import dloadbatch, setup_sesh
from eot.met_tseries import met_time_series
from tqdm import tqdm
import eot.eotimeseries as eot
import ee
import geopandas as gpd
import argparse
ee.Initialize()


parser = argparse.ArgumentParser()
parser.add_argument("-user", "--usr", type=str, required=True, 
                    help="CEDA username - required for MET data")

parser.add_argument("-pass", "--pss", type=str, required=True, 
                    help="CEDA password - required for MET data")

parser.add_argument("-cssfile", "--css", type=str, required=True, 
                    help="countryside survey point shapefile")

parser.add_argument("-folder", "--fldr", type=str, required=True, 
                    help="The path of the folder to work in")



args = parser.parse_args() 


#A bit of a kludge solution but a one off....
setup_sesh(args.usr, args.pss)

os.chdir(args.fldr)

# The input data
inShp = args.css

#template url - MET seem to update this semi regularly
rain_url16 = ('https://dap.ceda.ac.uk/badc/ukmo-hadobs/data/insitu/MOHC/'
 'HadOBS/HadUK-Grid/v1.0.2.1/1km/rainfall/mon/v20200731/'
 'rainfall_hadukgrid_uk_1km_mon_201601-201612.nc')
# prelim yr vars
years = ['201701-201712', '201701-201712', '201801-201812', '201901-201912',
         '201201-202012']

yrlist = [rain_url16.replace('201601-201612', y) for y in years]

# stick 2016 in
yrlist.insert(0, rain_url16)

# list of vars
clim_vars = ['groundfrost', 'hurs', 'psl', 'pv', 'sfcWind', 'sun', 'tas',
             'rainfall']

# wherever we are!
outdirs = ['2016', '2017', '2018', '2019']
_ = [os.mkdir(d) for d in outdirs if not os.path.isdir(d)]

# final list of urls
finalproc = []
for y in yrlist:
    sublist = [y.replace('rainfall', c) for c in clim_vars]
    finalproc.append(sublist)

# the met stuff
ootlists = []

for idx, yr in enumerate(finalproc):
    
    imlist = dloadbatch(yr, outdirs[idx])
    ootlists.append(imlist)
    for d,p in tqdm(zip(imlist, clim_vars)):
        met_time_series(d, inShp, inShp, p) 
        
  

        
        

        
        
        
    
