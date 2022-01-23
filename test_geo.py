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

def test_rivers_with_station():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    testList = []
    testList.append(MonitoringStation(s_id, m_id, label, (30.0,70.0), trange, 'River Wey', town))
    testList.append(MonitoringStation(s_id, m_id, label, (45.6,90.5), trange, 'River Way', town))
    testList.append(MonitoringStation(s_id, m_id, label, (30.0,70.0), trange, 'Costa Beck', town))
    testList.append(MonitoringStation(s_id, m_id, label, (45.6,90.5), trange, 'Ulley Brook', town))
    testList.append(MonitoringStation(s_id, m_id, label, (30.0,70.0), trange, 'Dean', town))
    testList.append(MonitoringStation(s_id, m_id, label, (45.6,90.5), trange, 'River Way', town))
    rivers = rivers_with_station(testList)
    assert len(rivers) == 5
    counter = 0
    for i in rivers:
        for j in rivers:
            if i == j:
                counter += 1
    assert counter == len(rivers)


def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    testList = []
    testList.append(MonitoringStation(s_id, m_id, 'Blackford Bridge', (30.0,70.0), trange, 'River Wey', town))
    testList.append(MonitoringStation(s_id, m_id, 'Shipley', (45.6,90.5), trange, 'River Way', town))
    testList.append(MonitoringStation(s_id, m_id, 'Chew Stoke', (30.0,70.0), trange, 'Costa Beck', town))
    testList.append(MonitoringStation(s_id, m_id, 'Chalford', (45.6,90.5), trange, 'Ulley Brook', town))
    testList.append(MonitoringStation(s_id, m_id, 'Kings Pond', (30.0,70.0), trange, 'Dean', town))
    testList.append(MonitoringStation(s_id, m_id, 'Saltaire', (45.6,90.5), trange, 'River Way', town))
    station_river = stations_by_river(testList)
    assert len(station_river) == 5
    assert station_river['River Wey'] == ['Blackford Bridge']
    assert station_river['River Way'] == ['Shipley', 'Saltaire']



def test_rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    testList = []
    testList.append(MonitoringStation(s_id, m_id, 'Blackford Bridge', (30.0,70.0), trange, 'River Way', town))
    testList.append(MonitoringStation(s_id, m_id, 'Shipley', (45.6,90.5), trange, 'River Way', town))
    testList.append(MonitoringStation(s_id, m_id, 'Chew Stoke', (30.0,70.0), trange, 'Costa Beck', town))
    testList.append(MonitoringStation(s_id, m_id, 'Chalford', (45.6,90.5), trange, 'Costa Beck', town))
    testList.append(MonitoringStation(s_id, m_id, 'Kings Pond', (30.0,70.0), trange, 'Dean', town))
    testList.append(MonitoringStation(s_id, m_id, 'Saltaire', (45.6,90.5), trange, 'River Way', town))
    assert len(rivers_by_station_number(testList,2)) == 2
    assert rivers_by_station_number(testList,2)[0][1] ==3