import matplotlib.pyplot as plt
from template import setup_plot
import csv
from uncertainties import unumpy
import numpy as np


fig, ax = plt.subplots()
setup_plot(ax, "Зависимость интенсивности пика от расстояния", "x, мм", "Интенсивность, отн. ед.")

arr = {
    "x": [],
    "I1": [],
    "I2": [],
    "I3": [],
    "sI1": [],
    "sI2": [],
    "sI3": [],
}


k = 0
data = csv.reader(open("data3.csv", "r"), delimiter=",")
for row in data:
    x, I1, sI1, I2, sI2, I3, sI3 = list(map(int, row))
    arr["x"].append(x)
    arr["I1"].append(I1)
    arr["sI1"].append(sI1)
    arr["I2"].append(I2)
    arr["sI2"].append(sI2)
    arr["I3"].append(I3)
    arr["sI3"].append(sI3)
    k += 1

ax.errorbar(
    arr["x"],
    arr["I1"],
    xerr=[0.05]*k,
    yerr=arr["sI1"],
    fmt="s",
    label="E=4.78 МэВ",
    linestyle="-"
)

ax.errorbar(
    arr["x"],
    arr["I2"],
    xerr=[0.05]*k,
    yerr=arr["sI2"],
    fmt="s",
    label="E=5.4 МэВ",
    linestyle="-"
)

ax.errorbar(
    arr["x"],
    arr["I3"],
    xerr=[0.05]*k,
    yerr=arr["sI3"],
    fmt="s",
    label="E=6 МэВ",
    linestyle="-"
)

ax.legend()
plt.show()
