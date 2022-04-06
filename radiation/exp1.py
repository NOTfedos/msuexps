from math import pow, sqrt, log

A = 48
Z = 22
mass = 1876
enrg = 70
dnst = 4.6
b2 = 1 - (mass / (mass + enrg))**2

sploss = 0.31 * Z * dnst * (11.2 + log(b2 / (Z*(1-b2))) - b2) / (A*b2)
print(sploss)
