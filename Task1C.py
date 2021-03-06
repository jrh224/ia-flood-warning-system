from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    stations = build_station_list()
    nameList = []
    for station in stations_within_radius(stations, (52.2053, 0.1218), 10):
        nameList.append(station.name)
    nameList.sort()
    print(nameList)



if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()