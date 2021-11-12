import pandas as pd
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
from template import setup_plot
from math import sqrt
import numpy as np
from scipy.optimize import curve_fit
from math import pi
import csv

arr = csv.reader(open("data1.csv"), delimiter=",", quoting=csv.QUOTE_NONNUMERIC)

s = 0
k = 0
for el in arr:
    k+=1
    s += abs(el[0] - el[1])

dx = s / k

print(f"{dx=}")

