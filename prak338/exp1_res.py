import pandas as pd
from uncertainties import unumpy, ufloat
import math
from template import setup_plot
from matplotlib import pyplot as plt


fig, ax = plt.subplots(1)
setup_plot(ax, rf"Зависимость толщины скин-слоя $\delta$ для образцов от частоты генератора $f$",
           r"$f$, $Гц$", r"$\delta$, см")


materials = ["Al", "Brass", "Cu", "Fe", "Pb", "Ti"]
mater = materials[0]
lims = (10, 10000)
mu = {
    "Al": 1, "Brass": 1, "Cu": 1, "Fe": 1400, "Pb": 1, "Ti": 1
}
mu_0 = 1.2566370614e-6

# тут ищем сигмы
data2 = pd.read_csv("./datadir/coefs.csv")
d = dict()
s_Cu = 60
A_Cu = ufloat(data2[data2["Mater"] == "Cu"]["A"].values[0], data2[data2["Mater"] == "Cu"]["sA"].values[0])
for index, row in data2.iterrows():
    sigma = ufloat(row["A"], row["sA"]) / A_Cu * s_Cu
    d.update({row["Mater"]: sigma})


for i, mater in enumerate(materials):
    data = pd.read_csv(f"./datadir/{mater}.txt", sep='\t')
    #print(data.columns)

    s_Cu = 60
    A_Cu = ufloat(data2[data2["Mater"] == mater]["A"].values[0], data2[data2["Mater"] == mater]["sA"].values[0])

    if i > 2:
        lims = (1000, 10000)
    else:
        lims = (10, 1000)
    data = data[data["  Hz"] > lims[0]][data["  Hz"] < lims[1]]

    x_arr = data["  Hz"].values
    y_arr = 1 / (math.pi * data["  Hz"] * mu[mater] * mu_0 * d[mater])**0.5 / 10

    #print(y_arr)

    ax.errorbar(x_arr, unumpy.nominal_values(y_arr),
                yerr=unumpy.std_devs(y_arr), fmt='o', label=mater, linewidth=2)

plt.legend()
plt.show()

