import matplotlib.pyplot as plt
from template import setup_plot
import csv
from uncertainties import unumpy
import numpy as np
from math import pi
from scipy.optimize import curve_fit


fig, ax = plt.subplots()
setup_plot(ax, "Зависимость напряжения на детекторе от угла", r"$\varphi$, $^{\circ}$", "U, В")

x = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
y = [135, 130, 125, 110, 85, 52, 30, 13, 5, 2]

xerr = [i / 20 for i in x]
yerr = [i / 20 for i in y]

ax.errorbar(
    x, y, xerr=xerr, yerr=yerr, fmt='s'
)


def f(x, a, b):
    return a*np.cos(x / 180 * pi)**2 + b


popt, perr = curve_fit(f, np.array(x), np.array(y))
print(popt, np.sqrt(np.diag(perr)))

ax.errorbar(x, f(np.array(x), *popt))

plt.show()

