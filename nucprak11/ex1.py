import pandas as pd
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from template import setup_plot
from math import sqrt
import numpy as np
from scipy.optimize import curve_fit

data = pd.read_excel("data1.xlsx")


data["ro"] = data["h"]*11.34
data["t"] = unumpy.uarray(y := data["t"], [1 for _ in y])
n_arr = unumpy.uarray(y := data["n"], np.sqrt(y)*1.2)
nt = n_arr / data["t"]
data["n/t"] = nt
x_arr = unumpy.uarray(y := data["ro"], [0.05*11.34 for el in y])

print(data)

fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости скорости $\frac{N}{t}$ счёта частиц от толщины фильтра $x$",
           r"$x$, $\frac{г}{{см}^{2}}$", r"$\frac{N}{t}$, ${с}^{-1}$")

ax.errorbar(unumpy.nominal_values(x_arr),
            unumpy.nominal_values(nt),
            xerr=unumpy.std_devs(x_arr),
            yerr=unumpy.std_devs(nt), fmt='s')


def f(x, a, b, c):
    return a * np.exp(-x/b) + c


popt, perr = curve_fit(f, unumpy.nominal_values(x_arr), unumpy.nominal_values(nt))
print(popt, np.sqrt(np.diag(perr)))
print(perr)
ax.errorbar(unumpy.nominal_values(x_arr), f(unumpy.nominal_values(x_arr), *popt), linewidth=2)

plt.show()
