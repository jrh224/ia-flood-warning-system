from floodsystem.analysis import polyfit, rising_polynomial, relative_risk
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import datetime
from floodsystem.stationdata import MonitoringStation


from floodsystem.stationdata import build_station_list, update_water_levels



stations = build_station_list()
update_water_levels(stations)
for station in stations:
    if station.name == 'Letcombe Bassett':
        print(relative_risk(station))

