from floodsystem.analysis import polyfit, rising_polynomial, relative_risk
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import datetime
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import MonitoringStation


from floodsystem.stationdata import build_station_list, update_water_levels



stations = build_station_list()
update_water_levels(stations)
lowstations = []
moderatestations = []
highstations = []
severestations = []
datalessstations = []
for station in stations:
    numericalrisk = relative_risk(station)
    try:

        if numericalrisk < 1:
            risk = 'low'
            lowstations.append((station.town, risk))
        elif numericalrisk == 1:
            risk = 'moderate'
            moderatestations.append((station.town, risk))
        elif numericalrisk == 2:
            risk = 'high'
            highstations.append((station.town, risk))
        elif numericalrisk > 2:
            risk = 'severe'
            severestations.append((station.town, risk))
    except:
        risk = 'not enough data'
        datalessstations.append((station.town, risk))
print(severestations)
print(highstations)
print(moderatestations)
print(lowstations)
print(datalessstations)



    



