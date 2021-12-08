from math import pow

hf = 2.5 * 24 * 3600
mass = 1000
A = 128

act = mass * 1e-6 / (2.4 * pow(10, -24) * hf * A)

print(act)
