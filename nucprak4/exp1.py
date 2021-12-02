import matplotlib.pyplot as plt
from template import setup_plot
import numpy as np
from scipy.optimize import curve_fit
from math import pi
from numpy import cos
from uncertainties import unumpy, ufloat


count = range(0, 22, 2)
n = [2557, 1172, 1148, 1123, 1119, 1109, 1111, 1109, 1108, 1102, 1102, 1957]
t = [10, 7, 12, 19, 30, 46, 89, 102, 173, 355, 654, 3370]

y_raw = unumpy.uarray(n, [el*0.03 for el in n]) / np.array(t)
y = np.log(unumpy.nominal_values(y_raw))
y_err = 1/(unumpy.nominal_values(y_raw)) * unumpy.std_devs(y_raw)

x = [0.065 + el*0.175 for el in count] + [1.040]
x_err = [0.005 + 0.005 for el in count] + [0.005]

fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости величины $ln(\frac{n}{t})$ от толщины поглотителя",
           r"$x$, $мм$", r"$ln(\frac{n}{t})$")




def f(x, a, b):
    return a*x + b


popt, perr = curve_fit(f, np.array(x[:-1]), np.array(y[:-1]))
print(popt, np.sqrt(np.diag(perr)))

ax.errorbar(x + [5], f(np.array(x+[5]), *popt))
ax.axhline(y[-1])

ax.errorbar(x, unumpy.nominal_values(y), x_err, y_err, fmt='s')
plt.show()
