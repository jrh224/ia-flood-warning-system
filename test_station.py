# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, (-3, 4), river, town)
    b = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    c = MonitoringStation(s_id, m_id, label, coord, (7, 2), river, town)
    assert a.typical_range_consistent() == True
    assert b.typical_range_consistent() == False
    assert c.typical_range_consistent() == False

def test_inconsistent_typical_range_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, (-3, 4), river, town)
    b = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    c = MonitoringStation(s_id, m_id, label, coord, (7, 2), river, town)
    assert inconsistent_typical_range_stations([a,b,c]) == [b.name,c.name]