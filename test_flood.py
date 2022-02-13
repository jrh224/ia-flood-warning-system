from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level


def test_stations_level_over_threshold():
    stations = build_station_list()
    testdata = stations_level_over_threshold(stations, 0.8)
    assert len(testdata) > 0
    assert type(testdata[1]) == tuple
    assert type(testdata[1][1]) == float

def test_stations_highest_rel_level():
    stations = build_station_list()
    test_data = stations_highest_rel_level(stations, 11)
    assert len(test_data) == 11
    assert MonitoringStation.relative_water_level(test_data[0]) > MonitoringStation.relative_water_level(test_data[1])
    




