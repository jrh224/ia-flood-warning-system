from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold


def test_stations_level_over_threshold():
    stations = build_station_list()
    testdata = stations_level_over_threshold(stations, 0.8)
    assert len(testdata) > 0
    assert type(testdata[1]) == tuple
    assert type(testdata[1][1]) == float



