from floodsystem.station import MonitoringStation
def stations_level_over_threshold(stations, tol):
    'When given a list of MonitoringStation objects and a tolerance, returns a list of tuples of station objects with relative water levels over that tolerance, and their relative water levels'
    from floodsystem.utils import sorted_by_key
    from floodsystem.station import inconsistent_typical_range_stations
    eliminate = inconsistent_typical_range_stations(stations)
    list_of_tuples = []
    from floodsystem.stationdata import update_water_levels
    update_water_levels(stations)
    for station in stations:
        if station in eliminate:
            continue

        rel_level = MonitoringStation.relative_water_level(station)
        if rel_level == None:
            continue
        if rel_level > tol:
            station_and_level = (station, rel_level)
            list_of_tuples.append(station_and_level)

    return sorted_by_key(list_of_tuples,1)

def stations_highest_rel_level(stations, N):
    'returns a list of the N stations objects at which the water level is highest, in descending order by relative level'
    from floodsystem.station import MonitoringStation
    from floodsystem.stationdata import update_water_levels
    from floodsystem.utils import sorted_by_key
    update_water_levels(stations)
    station_and_level = []
    for station in stations:
        level = MonitoringStation.relative_water_level(station)
        
        if level != None:
            station_and_level.append((station,level))
  
    sorted_by_key(station_and_level, 1, True )
    new_list = station_and_level[:N]
    list_of_stations = []
    for z in new_list:
        list_of_stations.append(z[0])
    
    return list_of_stations
