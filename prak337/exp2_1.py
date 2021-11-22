from uncertainties import unumpy, ufloat
import template
import pandas as pd
from matplotlib import pyplot

arr1 = [[8198, 7955, 7712, 7525, 7450, 7300], [6347, 6440, 6608, 6683, 6870, 6833]]
arr2 = [[8198, 7917, 7712, 7562, 7431, 7282], [6309, 6459, 6590, 6665, 6758, 6833]]
arr3 = [[8160, 7973, 7768, 7581, 7413, 7338], [6328, 6421, 6571, 6665, 6758, 6833]]

arr_1 = []
arr_1_std = []
arr_2 = []
arr_2_std = []

for i in range(6):
    mean_1 = (arr1[0][i] + arr2[0][i] + arr3[0][1]) / 3
    mean_2 = (arr1[1][i] + arr2[1][i] + arr3[1][1]) / 3
    std_1 = (((arr1[0][i] - mean_1) ** 2 + (arr2[0][i] - mean_1) ** 2 + (arr3[0][i] - mean_1) ** 2) / 6) ** 0.5
    std_2 = (((arr1[1][i] - mean_2) ** 2 + (arr2[1][i] - mean_2) ** 2 + (arr3[1][i] - mean_2) ** 2) / 6) ** 0.5
    arr_1.append(mean_1)
    arr_1_std.append(std_1)
    arr_2.append(mean_2)
    arr_2_std.append(std_2)

print(len(arr_1), len(arr_1_std))
print(len(arr_2), len(arr_2_std))

arr_f01 = unumpy.uarray(arr_1, arr_1_std)
arr_f02 = unumpy.uarray(arr_2, arr_2_std)

kek = []

for f1, f2 in zip(arr_f01, arr_f02):
    kek.append(2**0.5 * f1 * f2 / (f1**2 + f2**2)**(0.5))
    print(2**0.5 * f1 * f2 / (f1**2 + f2**2)**(0.5))

fig, ax = pyplot.subplots()
template.setup_plot(ax, r"Зависимость коэффициента связи от расстония $x$",
                    r"$X$", r"$L$, $мГн$")

x = [0, 5, 10, 15, 20, 25]

# ax.errorbar(
#     x, arr_1, yerr=arr_1_std, label=r'$f_{р1}$', fmt='s'
# )
# ax.errorbar(
#     x, arr_2, yerr=arr_2_std, label=r'$f_{р2}$', fmt='s'
# )
# ax.errorbar(
#     x, unumpy.nominal_values(kek), yerr=unumpy.std_devs(kek), label=r'$f_{0}$', fmt='s'
# )

L = ufloat(1.067, 0.005)
f0 = ufloat(7107, 16)
arr_L_m = []
arr_L_s = []

for f1, f2 in zip(arr_f01, arr_f02):
    L12 = L * ((f0 / f2)**2 - 1)
    arr_L_m.append(L12.nominal_value)
    arr_L_s.append(L12.std_dev)
    L12 = L * (-(f0 / f1) ** 2 + 1)
    arr_L_m.append(L12.nominal_value)
    arr_L_s.append(L12.std_dev)

x_ = [0,0,5,5,10,10,15,15,20,20,25,25]


L12 = unumpy.uarray(arr_L_m, arr_L_s)

k_arr = L12 / L

print(len(L12), len(k_arr))

ax.errorbar(
    x_, unumpy.nominal_values(k_arr), yerr=unumpy.std_devs(k_arr), fmt='s'
)

# ax.errorbar(
#     x_, arr_L_m, yerr=arr_L_s, fmt='s'
# )

ax.legend()
pyplot.show()
