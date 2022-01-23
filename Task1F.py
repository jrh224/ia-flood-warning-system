from floodsystem.stationdata import build_station_list
from floodsystem.station import *


def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    print(inconsistent_stations)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()