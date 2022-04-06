from math import log, log2, sqrt, pow


E = 50

Z = 29
A = 63

dnst = 8.93


b2 = 1 - (0.5 / (0.5 + E))**2
ionloss = 0.15 * Z * dnst * (7.25 + log(b2*E*1e6/(Z*Z*(1-b2))) - (2*sqrt(1-b2)-1+b2)*log(2)+1-b2+pow((1-sqrt(1-b2)),2)/8)/(A*b2)
radloss = Z * E * ionloss / 800
print(radloss)
