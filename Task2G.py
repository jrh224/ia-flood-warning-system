from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import datetime

from floodsystem.stationdata import build_station_list



def relative_risk(station):
    relative_risk = 0 
    dt = 2
    times_and_levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    polynomial, dateshift = polyfit(times_and_levels[0],times_and_levels[1],4)
    derivative = np.polyder(polynomial, 4)
    current_derivative = derivative(times_and_levels[0][-1])
    print(current_derivative)

stations = build_station_list()
relative_risk(stations[1])
