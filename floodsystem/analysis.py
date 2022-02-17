import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(dates, levels, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return poly, dates[-1]


