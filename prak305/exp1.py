from uncertainties import ufloat
from math import pi

r_1 = ufloat(8.6, 0.05) / 1e3
r_2 = ufloat(14.5, 0.05) / 1e3
h = ufloat(6.3, 0.05) / 1e3

R_1 = ufloat(24, 0.5)
R_3 = ufloat(39, 0.5) * 1e3
C = ufloat(4, 0.5) * 1e-6

N_1 = 500
N_2 = 570

C_x = 64
C_y = 1

n_1 = N_1 / pi / (r_1 + r_2)
n_2 = N_2 / pi / (r_1 + r_2)

S = (r_2 - r_1) * h

# петля гистерезиса
OA = ufloat(5, 0.5) / 1e3
OB = ufloat(21, 0.5) / 1e3
OC = ufloat(14, 0.5) / 1e3
OD = ufloat(26, 0.5) / 1e3

H_c = n_1 * OA * C_x / R_1
B_ost = R_3 * C * OC * C_y / N_2 / S
B_s = R_3 * C * OD * C_y / N_2 / S
H_s = n_1 * OB * C_x / R_1

print(f"n1 = {n_1}, n2 = {n_2}, S = {S}")
print(H_c, B_ost, B_s, H_s, sep='\n')
