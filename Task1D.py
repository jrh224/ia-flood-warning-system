from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

rivers = rivers_with_station(build_station_list())
print(len(rivers))
alpha_rivers = sorted(rivers)
print(alpha_rivers[0:10])

rivers_stations = stations_by_river(build_station_list())
print(sorted(rivers_stations['River Aire']))
print(sorted(rivers_stations['River Cam']))
print(sorted(rivers_stations['River Thames']))