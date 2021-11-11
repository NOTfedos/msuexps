from uncertainties import ufloat
from math import pi, sqrt

C = ufloat(0.47, 0.005) * 1e-6
A = ufloat(13.480, 0.020) * 3.3 / 2
f = ufloat(4160, 50)
df = ufloat(308, 10)

L = 1 / 4 / pi**2 / f**2 / C

Q = f/df
r = 1 / Q * (L / C)**(0.5)
b = r / 2 / L

print(f"L={L * 1e3} мГн")

print(f"Q={Q}")

print(f"r={r}")

print(f"b={b}, w={2*pi/(L*C)**(0.5)}")
