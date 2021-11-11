import pandas as pd
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from template import setup_plot
from math import sqrt
import numpy as np
from scipy.optimize import curve_fit
from math import pi

r = ufloat(6.03, 0.25)
R = 1
L = ufloat(3.11, 0.08) * 1e-3

data = pd.read_csv("ex2_b.csv")

data["A"] = data["A"] * 3.3 / 2

data["C"] = unumpy.uarray(y:=data["C"], [x / 100 for x in y]) * 1e-6
data["A"] = unumpy.uarray(y:=data["A"], [x / 100 for x in y])
data["f"] = unumpy.uarray(y:=data["f"], [10 for x in y])
data["df"] = unumpy.uarray(y:=data["df"], [x / 40 for x in y])

y1 = [1 / (R+r) * (L/C)**(0.5) for C in data["C"]]
y2 = [L/ (R+r) * 2*pi*f for f in data["f"]]

fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости добротности $Q$ от частоты $f$",
           r"$f$", r"$Q$")

ax.errorbar(unumpy.nominal_values(data["f"]),
            unumpy.nominal_values(y1),
            xerr=unumpy.std_devs(data["f"]),
            yerr=unumpy.std_devs(y1), fmt='s', label=r"$Q = \frac{1}{R+r} \sqrt{\frac{L}{C}}$")

ax.errorbar(unumpy.nominal_values(data["f"]),
            unumpy.nominal_values(y2),
            xerr=unumpy.std_devs(data["f"]),
            yerr=unumpy.std_devs(y2), fmt='s', label=r"$Q = \frac{L}{R+r} 2 \pi f$")

#
# def f(x, a, b):
#     return a*x+b

#
# popt, perr = curve_fit(f, unumpy.nominal_values(data["f"]), unumpy.nominal_values(y))
# print(popt, np.sqrt(np.diag(perr)))
#
# x_arr = data["f"]
# ax.errorbar(unumpy.nominal_values(x_arr), f(unumpy.nominal_values(x_arr), *popt), linewidth=2)
ax.legend()
plt.show()
