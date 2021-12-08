import matplotlib.pyplot as plt
from uncertainties import unumpy, ufloat
import template
import pandas as pd
from matplotlib import pyplot
from scipy.optimize import curve_fit
import numpy as np



y = [[0.059, 0.13, 0.26], [0.1, 0.22, 0.43], [0.16, 0.34, 0.67]]
y_err = [[0.003, 0.009, 0.014], [0.005, 0.012, 0.022], [0.008, 0.018, 0.03]]

x = [5.7, 35, 74]
x_err = [1.3, 3, 5]

fig, ax = pyplot.subplots()
template.setup_plot(ax, r"Зависимость индуцируемой ЭДС от площади катушки $S$",
                    r"$S$, ${см}^2$", r"$E$, $В$")

print(y_err[0])

ax.errorbar(
    x, y[0],
    xerr=x_err, yerr=y_err[0],
    label="f=300 Гц"
)

ax.errorbar(
    x, y[1],
    xerr=x_err, yerr=y_err[1],
    label="f=500 Гц"
)

ax.errorbar(
    x, y[2],
    xerr=x_err, yerr=y_err[2],
    label="f=800 Гц"
)

def f(x, a, b):
    return a*x + b


for i in range(3):
    print(x)
    print(y[i])
    popt, perr = curve_fit(f, np.array(x), np.array(y[i]))
    print(i+1, popt, np.sqrt(np.diag(perr)))
    ax.plot(x, f(np.array(x), *popt), label=f"{i+1} appr")

ax.legend()
pyplot.show()
