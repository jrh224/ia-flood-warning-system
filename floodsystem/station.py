# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    
    def typical_range_consistent(self):
        "evaluates whether a monitor station object has inconsistent range data"
        if self.typical_range == None:
            return False
        elif (self.typical_range[1]<self.typical_range[0]):
            return False
        else:
            return True

    def relative_water_level(self):
        "returns latest water level as a fraction of the typical range"
      
        Latest_level = self.latest_level
        if self.typical_range_consistent() == False or Latest_level == None:
            return None
        else:
            typical_range = self.typical_range
            fraction = (Latest_level-typical_range[0])/(typical_range[1]-typical_range[0])
            return fraction

   
def inconsistent_typical_range_stations(stations):
    "returns a list of stations which have inconsistent range data"
    inconsistent_stations = []
    for station in stations:
        if not station.typical_range_consistent():
            inconsistent_stations.append(station.name)
    return sorted(inconsistent_stations)
