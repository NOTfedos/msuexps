import matplotlib.pyplot as plt
from template import setup_plot
from scipy.optimize import curve_fit
import numpy as np

y = [9.4, 17.2, 23.5]
yerr = [0.1, 0.3, 0.17]
x = [4.782, 5.4, 6.002]

y = [(i + 16)/10 for i in y]
x = [i**(3/2) for i in x]

fig, ax = plt.subplots()
setup_plot(ax, r"Зависимость расстояния $R_{\alpha}$ от $E^{\frac{3}{2}}$",
           r"$E^{\frac{3}{2}}$, $МэВ^{\frac{3}{2}}$",
           r"$R_{\alpha}$, мм", )

ax.errorbar(
    x,
    y,
    yerr=yerr,
    fmt='s'
)


def f(x, a):
    return a*np.array(x)


popt, perr = curve_fit(f, x, np.array(y))
print(popt, np.sqrt(np.diag(perr)))

ax.plot(x + [0], f(x + [0], *popt))

plt.show()
