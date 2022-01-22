from floodsystem.geo import *
from floodsystem.station import MonitoringStation

def test_stations_within_radius():
    # Create a test station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    testList = []
    testList.append(MonitoringStation(s_id, m_id, label, (52.2052, 0.1219),trange, river, town))
    testList.append(MonitoringStation(s_id, m_id, label, (100.2053, 87.1219),trange, river, town))
    
    assert stations_within_radius(testList, (52.2053, 0.1218), 10)

def test_stations_by_distance():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    testList = []
    testList.append(MonitoringStation(s_id, m_id, label, (30.0,70.0), trange, river, town))
    testList.append(MonitoringStation(s_id, m_id, label, (45.6,90.5), trange, river, town))
    a = stations_by_distance(testList,(23,45.88)) 
    b = stations_by_distance(testList, (30,70))
    assert len(a) == 2
    assert b[0][1] == 0
