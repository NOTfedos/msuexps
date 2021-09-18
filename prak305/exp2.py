import pandas as pd
from math import pi
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from template import setup_plot


data = pd.read_excel("data2.xlsx")

r_1 = ufloat(8.6, 0.05) / 1e3
r_2 = ufloat(14.5, 0.05) / 1e3
h = ufloat(6.3, 0.05) / 1e3

R_1 = ufloat(24, 0.5)
R_3 = ufloat(39, 0.5) * 1e3
C = ufloat(4, 0.005) * 1e-6

N_1 = 500
N_2 = 570

C_x = 64
C_y = 1

n_1 = N_1 / pi / (r_1 + r_2)
n_2 = N_2 / pi / (r_1 + r_2)

S = (r_2 - r_1) * h

data['OB'] = unumpy.uarray(data['OB'], [0.5 for _ in data['OB']]) * 1e-3
data['OD'] = unumpy.uarray(data['OD'], [0.5 for _ in data["OD"]]) * 1e-3

data['H'] = n_1 * data["OB"] * C_x / R_1
data['B'] = R_3 * C * data["OD"] * C_y / N_2 / S

data['mu'] = data['B'] / data['H'] / 4e-7 / pi

print(data)

fig, ax = plt.subplots()
setup_plot(ax, r"Зависимость магнитной проницаемости $\mu$ образца от напряженности $H$ внешнего магнитного поля",
           r"$H$, $\frac{А}{м}$", r"$\mu$")

# ax.errorbar(unumpy.nominal_values(data["H"]),
#             unumpy.nominal_values(data["B"]),
#             xerr=unumpy.std_devs(data["H"]),
#             yerr=unumpy.std_devs(data["B"]),
#             linewidth=3, fmt='s')

ax.errorbar(unumpy.nominal_values(data["H"]),
            unumpy.nominal_values(data["mu"]),
            xerr=unumpy.std_devs(data["H"]),
            yerr=unumpy.std_devs(data["mu"]),
            linewidth=3, fmt='s')

# plt.savefig("./plots/plt1.png")
plt.show()
