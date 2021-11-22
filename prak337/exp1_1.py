from uncertainties import ufloat
from math import pi

f = ufloat(7107, 16)
df = ufloat(570, 30)

Q = f/df

print("Q=",f/df)

C = 0.47e-6
L = 1 / C * (1/2/pi/f)**2
print("L=", L)

r = 1/Q * (L/C)**0.5
print("R=", r)
