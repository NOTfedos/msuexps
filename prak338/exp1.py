import pandas as pd
from math import pi
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from template import setup_plot
from scipy.optimize import curve_fit
import numpy as np


lims = (0, 1000)

data = pd.read_csv("./datadir/Empty.txt", sep='\t')
data = data[data["  Hz"] > lims[0]][data["  Hz"] < lims[1]]
print(data.columns)
fig, ax = plt.subplots(1)
setup_plot(ax, r"Зависимость тангенса разности фаз $tg(\varphi)$ в отсутствие сердечника от частоты генератора $f$",
           r"$f$", r"$tg(\varphi)$")

ax.errorbar(data["  Hz"], data["deg"],
            xerr=[0.005*x for x in data["  Hz"]],
            yerr=[0.005*x for x in data["deg"]],
            fmt='o')


def f(x, a, b):
    return a*x + b


popt, perr = curve_fit(f, data["  Hz"], data["deg"])
print(popt, np.sqrt(np.diag(perr)))

# ax.errorbar(y := np.arange(lims[0], lims[1]), f(y, *popt), linewidth=2)

plt.show()
