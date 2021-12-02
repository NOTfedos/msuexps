from uncertainties import ufloat


r = ufloat(4.47, 0.02)

r = 2.7 * r / 10
print(r)

E = (r / 0.4) ** (1/1.4)

print(E)

E = (r + 0.133) / 0.54

print(E)
