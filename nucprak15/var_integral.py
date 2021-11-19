from uncertainties import ufloat
from math import log, e


I_sp = ufloat(36500, 150)
I_a = ufloat(1918440, 571)

p_sp = I_sp / (I_a + I_sp)
p_a = I_a / (I_a + I_sp)

print(f"{p_sp=}", f"{p_a=}", sep='\n')

k = p_sp / p_a
print(f"{k=}")

print("--------------------------------------------------------")


t1 = 2.65 * (1 + 1/k)
t2 = 2.65 * (1 + k)

print(f"{t1=}", f"{t2=}", sep='\n')


