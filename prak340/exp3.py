import matplotlib.pyplot as plt
from template import setup_plot
import numpy as np
from scipy.optimize import curve_fit


fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости угла детектора $\phi$ от угла поворота пластины $\varphi$",
           r"$\varphi$, $^{\circ}$", r"$\phi$, $^{\circ}$")

x = [30, 40, 50, 60]
y = [120, 100, 85, 65]

# for i, el in enumerate(y):
#     y[i] = 180 - y[i] - x[i]

x_err = [0]*4
y_err = [5]*4


def f(x, a, b):
    return a*x+b


popt, perr = curve_fit(f, np.array(x), np.array(y))
print(popt, np.sqrt(np.diag(perr)))

ax.errorbar(x, f(np.array(x), *popt))

ax.errorbar(x, y, x_err, y_err, fmt='s')
plt.show()
