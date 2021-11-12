import matplotlib.pyplot as plt
from template import setup_plot
import numpy as np
from scipy.optimize import curve_fit
from math import pi
from numpy import cos

fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости напряжения на детектора $U$ от угла поворота $\varphi$",
           r"$\varphi$, $^{\circ}$", r"$U$, $В$")

x = [-25, 27, 35, -40, 0]
y = [3.6, 3.6, 4.4, 4.2, 6]

x_err = [0.1]*5
y_err = [0.05]*5

ax.errorbar(x, y, x_err, y_err, fmt='s')
plt.show()
