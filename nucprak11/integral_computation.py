from uncertainties import ufloat
import numpy as np
from math import pow
import colorama
colorama.init()


# a = ufloat(24, 0.5) / 100
# b = ufloat(24, 0.5) / 100
# d = ufloat(37, 0.5) / 100
a = 24.5
b = 24.5
d = 37
Integral = 0

num = 100

dx1 = a / num
dx2 = a / num
dy1 = a / num
dy2 = a / num
for x1 in np.linspace(0, a, num):
    print("\r\033[KProgress {:%}".format(x1 / a), flush=True, end='')
    for x2 in np.linspace(0, a, num):
        for y1 in np.linspace(0, b, num):
            for y2 in np.linspace(0, b, num):
                Integral += dx1 * dx2 * dy1 * dy2 * d / ((x1 - x2)**2 + (y1 - y2)**2 + d**2)**(3/2)

print('\n', Integral)

