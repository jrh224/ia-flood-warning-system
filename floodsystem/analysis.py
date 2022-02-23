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
    
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    dates = matplotlib.dates.date2num(dates)

    polynomial, dateshift = polyfit(dates, levels, 4)
    derivative = polynomial.deriv()
    print(polynomial)
    print(derivative)
