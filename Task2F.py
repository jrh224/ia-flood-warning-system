from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    #Build stations list
    stations = build_station_list()

    #Update water levels
    update_water_levels(stations)

    #Remove stations without water data
    stations_with_water = []
    for station in stations:
        if station.latest_level != None:
            stations_with_water.append(station)

    sorted_by_water = sorted(stations_with_water, key=lambda MonitoringStation: MonitoringStation.latest_level, reverse=True)
    i = 0
    j = 0
    while j < 6:
        dates, levels = fetch_measure_levels(sorted_by_water[i].measure_id, dt=datetime.timedelta(days=2))

        try:
            plot_water_level_with_fit(sorted_by_water[i], dates, levels, 4)
            i+=1
            j+=1
        except:
            print(sorted_by_water[i].name + ' did not have enough data for the past two days and so cannot be plotted.')
            i+=1

run()