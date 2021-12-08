import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy, ufloat
import template
from scipy.optimize import curve_fit
import pandas as pd
from matplotlib import pyplot


y = [
    [0.08, 0.16, 0.25, 0.33, 0.43, 0.51, 0.59, 0.67, 0.75, 0.82],
    [0.05, 0.09, 0.13, 0.17, 0.22, 0.26, 0.31, 0.34, 0.39, 0.43],
    [0.06, 0.13, 0.18, 0.24, 0.31, 0.37, 0.42, 0.48, 0.53, 0.57],
    [0.03, 0.07, 0.09, 0.13, 0.16, 0.18, 0.22, 0.26, 0.29, 0.32],
    [0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.13, 0.15, 0.18, 0.2]
]
y_err = [
    [0.007, 0.01, 0.014, 0.018, 0.022, 0.026, 0.03, 0.03, 0.04, 0.04],
    [0.003, 0.005, 0.009, 0.010, 0.013, 0.014, 0.017, 0.018, 0.020, 0.022],
    [0.007, 0.009, 0.011, 0.013, 0.017, 0.020, 0.022, 0.025, 0.028, 0.03],
    [0.0016, 0.004, 0.005, 0.007, 0.008, 0.009, 0.011, 0.013, 0.015, 0.016],
    [0.0012, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.009]
]

x = [144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440]
x_err = [8, 15, 23, 30, 38, 46, 53, 61, 68, 76]

fig, ax = pyplot.subplots()
template.setup_plot(ax, r"Зависимость индуцируемой ЭДС от величины $\frac{dI}{dt}$",
                    r"$\frac{dI}{dt}$, $\frac{А}{с}$", r"$E$, $В$")

for i in range(5):
    ax.errorbar(
        x, y[i],
        xerr=x_err, yerr=y_err[i],
        label=str(i+1),
        fmt="s"
    )


def f(x, a, b):
    return a*x + b


for i in range(5):
    print(x)
    print(y[i])
    popt, perr = curve_fit(f, np.array(x), np.array(y[i]))
    print(i+1, popt, np.sqrt(np.diag(perr)))
    ax.plot(x, f(np.array(x), *popt), label=f"{i+1} appr")

ax.legend()
pyplot.show()
