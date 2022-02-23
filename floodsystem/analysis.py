import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def polyfit(dates, levels, p):

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return poly, dates[-1]


def rising_polynomial(station):
    #Find slope of station and return true if positive at most recent value

    #Extract water levels over last 2 days
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    dates = matplotlib.dates.date2num(dates)

    #Shift dates to make polyfit function more stable
    datesShifted = []
    for date in dates:
        datesShifted.append(date - dates[-1])
    
    #Find polynomial and first derivative
    polynomial, dateshift = polyfit(datesShifted, levels, 4)
    derivative = polynomial.deriv()
    
    #Find slope at final date value
    finalSlope = np.polyval(derivative, datesShifted[0])

    #Return true if slope is positive
    if finalSlope > 0:
        return True
    else:
        return False
