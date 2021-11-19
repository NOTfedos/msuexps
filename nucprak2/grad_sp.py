import matplotlib.pyplot as plt
from template import setup_plot
from scipy.optimize import curve_fit
from uncertainties import unumpy
import numpy as np


fig, ax = plt.subplots()
setup_plot(ax, "Зависимость энергии от канала", "Номер канала", "Энергия, МэВ")


x1 = [383, 483, 516, 602, 877]
x2 = [20, 20, 23, 25, 19]
y = [4.782, 5.305, 5.490, 6.002, 7.687]
y = unumpy.uarray(y, [0]*5)
x = unumpy.uarray(x1, x2)


def f(x, a, b):
    return a*x + b


popt, perr = curve_fit(f, unumpy.nominal_values(x), unumpy.nominal_values(y))
print(popt, np.sqrt(np.diag(perr)))

ax.errorbar(unumpy.nominal_values(x),
            unumpy.nominal_values(y),
            xerr=unumpy.std_devs(x),
            yerr=unumpy.std_devs(y),
            fmt='s')

ax.plot(unumpy.nominal_values(x), f(unumpy.nominal_values(x), *popt))

plt.show()
