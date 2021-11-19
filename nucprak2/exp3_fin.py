import matplotlib.pyplot as plt
from template import setup_plot
import csv
from uncertainties import unumpy
import numpy as np


def grad(arr):
    global a, b
    return [a*x for x in arr]


fig, ax = plt.subplots()
setup_plot(ax, "Зависимость полуширины пика от расстояния", "x, мм", "Энергия, МэВ")

a = 0.0059
b = 2.46

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

ax.plot(
    arr["x"],
    grad(arr["sI1"]),
    label="E=4.78 МэВ"
)

ax.plot(
    arr["x"],
    grad(arr["sI2"]),
    label="E=5.4 МэВ",
)

ax.plot(
    arr["x"],
    grad(arr["sI3"]),
    label="E=6 МэВ",
)

plt.show()
