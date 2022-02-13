from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    "Requirement for task 1E"
    rivers = rivers_by_station_number(build_station_list(), 10)
    print(rivers)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()