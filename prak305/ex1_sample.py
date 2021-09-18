from template import setup_plot
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import unumpy
import numpy as np


fig, ax = plt.subplots()
# setup_plot(ax, r"Зависимость анодного тока от анодного напряжения на диоде $I(U^{\frac{3}{2}})$",
#            r"$U^{\frac{3}{2}}$, $В^{\frac{3}{2}}$", r"$I$, $мА$")

setup_plot(ax, r"Зависимость анодного тока от анодного напряжения на диоде $I(U)$",
           r"$U$, $В$", r"$I$, $мА$")

data = pd.read_csv("table1.csv")
I_un = unumpy.uarray(y := data.loc[:, "I"], [0.01 for _ in range(len(y))])
U_un = unumpy.uarray(y := data.loc[:, "U"], [0.5 for _ in range(len(y))])

print(U_un)


def f(x, a):
    return a * x


# popt, perr = curve_fit(f, unumpy.nominal_values(U_un), unumpy.nominal_values(I_un))
# print(popt, np.sqrt(np.diag(perr)))
# ax.errorbar(unumpy.nominal_values(U_un), f(unumpy.nominal_values(U_un), *popt), linewidth=2)

ax.errorbar(unumpy.nominal_values(U_un),
            unumpy.nominal_values(I_un),
            xerr=unumpy.std_devs(U_un),
            yerr=unumpy.std_devs(I_un), fmt='s')

plt.savefig("test.png")
plt.show()