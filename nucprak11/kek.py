from uncertainties import ufloat
from math import pow

a = ufloat(24, 0.5) / 100
b = ufloat(24, 0.5) / 100
d = ufloat(37, 0.5) / 100

print(((24/100-a)**2 + (24/100-b)**2 + d**2)**(-3/2))

a0 = a - 24/100
b0 = b - 24/100

print(((0-a)**2 + (0-b)**2 + d**2)**(-3/2))
