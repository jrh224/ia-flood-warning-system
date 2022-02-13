from floodsystem.stationdata import MonitoringStation, build_station_list
from floodsystem.flood import stations_level_over_threshold

   
def run():
    "Requirement for task 2B"
    stations = build_station_list()
    for x in stations_level_over_threshold(stations, 0.8):
        data = x[0]
        print(data.name, x[1])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()





