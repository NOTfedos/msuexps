from uncertainties import unumpy, ufloat
import template
import pandas as pd
from matplotlib import pyplot
arr1 = [[7093, 7082, 7092, 7058, 7070], [7092, 7082, 7092, 7081, 7081], [7095, 7081, 7092, 7059, 7075]]
arr2 = [[8379, 9084, 9858, 14104, 16595], [8378, 9073, 9835, 14104, 15947], [8391, 9085, 9842, 14104, 16431]]

arrf1m = []
arrf1s = []
arrf2m = []
arrf2s = []

for i in range(5):
    arrf1m.append((arr1[0][i] + arr1[1][0] + arr1[2][0]) / 3)
    print(arr1[2][i])
    arrf1s.append((((arr1[0][i] - arrf1m[i])**2 + (arr1[1][i] - arrf1m[i])**2 + (arr1[2][i] - arrf1m[i])**2) / 6)**0.5)
    arrf2m.append((arr2[0][i] + arr2[1][i] + arr2[2][i]) / 3)
    arrf2s.append((((arr2[0][i] - arrf2m[i]) ** 2 + (arr2[1][i] - arrf2m[i]) ** 2 + (arr2[2][i] - arrf2m[i])**2) / 6) ** 0.5)

arr1 = unumpy.uarray(arrf1m, arrf1s)
arr2 = unumpy.uarray(arrf2m, arrf2s)

y = (arr2)**2 - (arr1)**2

x = [2.04, 1.40, 0.95, 0.31, 0.22]
x = [2 / i for i in x]

fig, ax = pyplot.subplots()
template.setup_plot(ax, r"Зависимость $f_{02}^{2} - f_{01}^{2}$ от велчииы $\frac{2}{C_{св}}$",
                    r"$\frac{2}{C_{св}}$, $\frac{1}{мкФ}$", r"$f_{02}^{2} - f_{01}^{2}$, $Гц^{2}$")

print(y)

ax.errorbar(
    x, unumpy.nominal_values(y), yerr=unumpy.std_devs(y), fmt='s'
)

pyplot.show()