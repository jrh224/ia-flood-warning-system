from floodsystem.analysis import *
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from dateutil.tz import tzutc
from random import randint

def test_polyfit():

    #Initialise sample water level data for an arbitrary station
    dates = [datetime.datetime(2022, 2, 18, 14, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 14, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 14, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 14, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 13, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 13, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 13, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 13, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 12, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 12, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 12, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 12, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 11, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 11, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 11, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 11, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 10, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 10, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 10, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 10, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 9, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 9, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 9, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 9, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 8, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 8, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 8, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 8, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 7, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 7, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 7, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 7, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 6, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 6, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 6, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 6, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 5, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 5, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 5, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 5, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 4, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 4, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 4, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 4, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 3, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 3, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 3, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 3, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 2, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 2, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 2, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 2, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 1, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 1, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 1, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 1, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 0, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 0, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 0, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 18, 0, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 23, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 23, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 23, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 23, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 22, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 22, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 22, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 22, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 21, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 21, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 21, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 21, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 20, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 20, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 20, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 20, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 19, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 19, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 19, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 19, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 18, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 18, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 18, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 18, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 17, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 17, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 17, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 17, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 16, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 16, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 16, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 16, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 15, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 15, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 15, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 15, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 14, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 14, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 14, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 14, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 13, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 13, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 13, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 13, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 12, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 12, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 12, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 12, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 11, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 11, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 11, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 11, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 10, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 10, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 10, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 10, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 9, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 9, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 9, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 9, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 8, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 8, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 8, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 8, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 7, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 7, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 7, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 7, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 6, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 6, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 6, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 6, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 5, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 5, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 5, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 5, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 4, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 4, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 4, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 4, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 3, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 3, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 3, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 3, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 2, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 2, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 2, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 2, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 1, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 1, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 1, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 1, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 0, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 0, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 0, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 17, 0, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 23, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 23, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 23, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 23, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 22, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 22, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 22, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 22, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 21, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 21, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 21, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 21, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 20, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 20, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 20, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 20, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 19, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 19, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 19, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 19, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 18, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 18, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 18, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 18, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 17, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 17, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 17, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 17, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 16, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 16, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 16, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 16, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 15, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 16, 15, 30, tzinfo=tzutc())]
    levels = [0.243, 0.246, 0.248, 0.251, 0.254, 0.257, 0.261, 0.264, 0.267, 0.27, 0.271, 0.272, 0.272, 0.271, 0.269, 0.265, 0.261, 0.256, 0.251, 0.247, 0.24, 0.234, 0.227, 0.22, 0.213, 0.207, 0.203, 0.199, 0.195, 0.192, 0.191, 0.189, 0.187, 0.186, 0.185, 0.184, 0.184, 0.183, 0.183, 0.183, 0.183, 0.182, 0.182, 0.182, 0.182, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.181, 0.182, 0.182, 0.182, 0.182, 0.183, 0.183, 0.183, 0.183, 0.183, 0.184, 0.184, 0.184, 0.184, 0.185, 0.185, 0.185, 0.185, 0.185, 0.186, 0.186, 0.186, 0.187, 0.187, 0.187, 0.187, 0.188, 0.188, 0.188, 0.189, 0.189, 0.19, 0.19, 0.19, 0.191, 0.191, 0.191, 0.191, 0.192, 0.192, 0.192, 0.193, 0.193, 0.194, 0.194, 0.195, 0.195, 0.196, 0.196, 0.196, 0.197, 0.197, 0.198, 0.198, 0.199, 0.199, 0.199, 0.2, 0.2, 0.2, 0.201, 0.201, 0.202, 0.202, 0.203, 0.203, 0.204, 0.204, 0.205, 0.205, 0.206, 0.207, 0.207, 0.207, 0.208, 0.208, 0.209, 0.21, 0.21, 0.211, 0.211, 0.212, 0.213, 0.213, 0.214, 0.214, 0.215, 0.215, 0.216, 0.217, 0.218, 0.218, 0.219, 0.219, 0.22, 0.221, 0.221, 0.222, 0.222, 0.223, 0.223, 0.224, 0.224, 0.225, 0.225, 0.226, 0.226, 0.227, 0.227, 0.227, 0.228, 0.229, 0.23, 0.23, 0.231, 0.231, 0.232, 0.232, 0.233, 0.234, 0.235, 0.235, 0.236, 0.237, 0.237, 0.238, 0.239, 0.239, 0.24, 0.241, 0.242, 0.242, 0.243, 0.243]

    datesConverted = matplotlib.dates.date2num(dates)

    datesShifted = []

    for i in datesConverted:
        datesShifted.append(i - datesConverted[0])


    try:
        polyfit(datesShifted, levels, 4)
    except:
        assert False

def test_relative_risk():
    stations = build_station_list()
    testlist = []
    for i in range(10):
        testlist.append(relative_risk(stations[i]))
    assert len(testlist) == 10
    for j in range(10):
        if testlist[j] != None:
            assert testlist[j] < 6
            assert testlist[j] > -2
     
    
        


def test_rising_polynomial():
    #create test data
    stations = build_station_list()
    update_water_levels(stations)

    randomStations = []
    for i in range(30):
        randomStations.append(randint(0,len(stations)-1))

    successes = 0

    for SIndex in randomStations:
        try:
            rising_polynomial(stations[SIndex])
            successes += 1
        except:
            pass

    assert successes > 15


    
    
    


