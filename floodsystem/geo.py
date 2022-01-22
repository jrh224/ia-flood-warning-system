# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_within_radius(stations, centre, r):
    from haversine import haversine, Unit
    true_stations = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            true_stations.append(station)
    return(true_stations)

