# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import importlib
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    "Takes a list of station data in the MonitoringStation form, and a coordinate and returns a list of tuples of the station name and its distance from that point."
    l = []
    for e in stations:
        Station = None
        if "station_id" in e:
            Station = e["station_id"]
        Coord = None
        if "coord" in e:
            Coord = e["coord"]
        Distance = haversine(Coord,p)
        p = (Station, Distance)
        l.append(p)
    return sorted_by_key(l)


def stations_within_radius(stations, centre, r):
    true_stations = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            true_stations.append(station)
    return(true_stations)



