from floodsystem.analysis import polyfit, rising_polynomial
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np


from floodsystem.stationdata import build_station_list



stations = build_station_list()

rising_polynomial(stations[6])
