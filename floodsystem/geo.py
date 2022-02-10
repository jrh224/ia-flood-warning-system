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
    "Takes a list of MonitoringStation objects, a coordinate and a radius and returns a list of all the stations within that radius of the coordinate"
    true_stations = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            true_stations.append(station)
    return(true_stations)

def  rivers_with_station(stations):
    "given a list of station objects, returns a set with the names of the rivers with a monitoring station"
    rivers = set()
    for e in stations:
        rivers.add(e.river)
    return rivers

def stations_by_river(stations):
    "Takes a list of MonitoringStation objects and returns a dictionary mapping river names to a list of stations on that river"
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
   
def rivers_by_station_number(stations, N):
    "Takes a list of MonitoringStation objects and a number N and returns a list of N (river name, number of stations) tuples, with the highest number of stations, sorted by the number of stations"
    from.geo import stations_by_river
    stat_river = stations_by_river(stations)
    river_and_number = []
    for river in stat_river:
        number = len(stat_river[river])
        river_and_number.append((river,number))
    ordered = sorted_by_key(river_and_number,1,reverse=True)
    return ordered[:N]







