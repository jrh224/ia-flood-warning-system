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

