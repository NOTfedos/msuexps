from math import pow, sqrt, log

A = 208
Z = 82
mass = 938
enrg = 50
dnst = 11.35
b2 = 1 - (mass / (mass + enrg))**2

sploss = 0.31 * Z * dnst * (11.2 + log(b2 / (Z*(1-b2))) - b2) / (A*b2)
print(sploss)
