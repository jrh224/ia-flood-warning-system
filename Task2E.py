from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    #Build stations list
    stations = build_station_list()

    #Update water levels
    update_water_levels(stations)

    #Remove stations without water level data
    stations_with_water = []
    for station in stations:
        if station.latest_level != None:
            stations_with_water.append(station)

    #Sort stations by water level and create list with just staion name and water level
    sorted_by_water = sorted(stations_with_water, key=lambda MonitoringStation: MonitoringStation.latest_level, reverse=True)
    

    for i in range(5):
        dates, levels = fetch_measure_levels(sorted_by_water[i].measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(sorted_by_water[i], dates, levels)


run()


