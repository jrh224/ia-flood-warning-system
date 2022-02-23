from floodsystem.plot import *
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels


def test_plot_water_levels():
    #create test data
    stations = build_station_list()
    update_water_levels(stations)

    #test that there is water data for the plot function for at least 5 stations
    stations_with_water_data = 0

    for station in stations:
        if station.latest_level != None and station.latest_level != '':
            stations_with_water_data += 1
    
    assert stations_with_water_data > 5
