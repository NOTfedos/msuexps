from math import log


E = 100

z_a = 47
m_a = 108
p_a = 10.5

z_b = 26
m_b = 56
p_b = 7.874

k = z_a * p_a * m_b / z_a / p_b / m_a * log(4 * 0.511 * E / 1875.613 / z_a / 13.5 * 10**6) / \
    log(4 * 0.511 * E / 1875.613 / z_b / 13.5 * 10**6)

print(k)
