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
        Station = e.name
        
        Coord = e.coord
        Distance = haversine(Coord,p)
        z = (Station, Distance)
        l.append(z)
    return sorted_by_key(l,1)

def stations_within_radius(stations, centre, r):
    true_stations = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            true_stations.append(station)
    return(true_stations)

def  rivers_with_station(stations):
    rivers = set()
    for e in stations:
        rivers.add(e.river)
    return rivers

def stations_by_river(stations):
    from .geo import rivers_with_station
    stat_river = {}
    rivers = rivers_with_station(stations)
    for i in rivers:
        station_list = []
        for j in stations:
            if i == j.river:
                station_list.append(j.name)
            stat_river[i] = station_list
    return stat_river
   

