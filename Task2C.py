from floodsystem.stationdata import MonitoringStation, build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    "Requirement for task 2C"
    stations = build_station_list()
    x = (stations_highest_rel_level(stations, 10))
    
    for i in x:
        level = MonitoringStation.relative_water_level(i)
        print(i.name, level)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

