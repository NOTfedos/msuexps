from uncertainties import ufloat

I_max = ufloat(3, 0.5)
I_min = ufloat(2, 0.5)

k = (I_max - I_min) / (I_max + I_min)

print(k)
