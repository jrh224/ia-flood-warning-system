from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    "Requirements for task 1B"
    a = build_station_list()
    station_distance = stations_by_distance(a,(52.2053, 0.1218))
    station_town_distance = []
    for i in range(len(station_distance)):
        Station = station_distance[i][0]
        Distance = station_distance[i][1]
        for e in a:
            if e.name == Station:
                Town = e.town
        station_town_distance.append((Station,Town,Distance))
    print(station_town_distance[0:9])
    print(station_town_distance[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
