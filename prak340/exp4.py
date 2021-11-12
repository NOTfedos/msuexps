import matplotlib.pyplot as plt
from template import setup_plot
import numpy as np
from scipy.optimize import curve_fit
from math import pi
from numpy import cos

fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости напряжения на детектора $U$ от угла поворота $\varphi$",
           r"$\varphi$, $^{\circ}$", r"$U$, $В$")

x = range(0, 50, 5)
y = [6.4, 6.4, 6.5, 6.4, 6.4, 6.3, 6.2, 6, 5.5, 5.2]

y = list(map(lambda x: x * 2, y))

x_err = [0.1]*10
y_err = [0.2]*10


def f(x, a, b):
    return a*cos(x / 180 * pi)**2 + b


popt, perr = curve_fit(f, np.array(x), np.array(y))
print(popt, np.sqrt(np.diag(perr)))

ax.errorbar(x, f(np.array(x), *popt))

ax.errorbar(x, y, x_err, y_err, fmt='s')
plt.show()
