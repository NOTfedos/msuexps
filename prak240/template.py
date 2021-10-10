import matplotlib.pyplot as plt
import numpy as np
from math import log

x = []
y = []
for line in open("data.txt"):
    t, p1, p = list(map(float, line.split(" ")))
    x.append(t)
    y.append(log(p1 / p))

#---------------------------/ Graphics /--------------------------

fig, ax = plt.subplots()

ax.minorticks_on()
ax.grid(which='major', linewidth=0.5, linestyle='dashed', color='black')

#устанавливаем подпись
ax.set_title(r"Зависимость $ln{\frac{\Delta p_1}{\Delta p}}$ от времени задержки $t$")

#делаем штрихи внутрь
ax.tick_params(which='major', direction='in', width=1.5, length=8)
ax.tick_params(which='minor', direction='in', width=1.5, length=4)

#устанавливаем подписи к осям
ax.set_xlabel(r't, с', fontsize='large')
ax.set_ylabel(r'$ln{\frac{\Delta p_1}{\Delta p}}$', fontsize='large')

#ax.axhline(linewidth=3)
#ax.axvline(linewidth=3)    


# Погрешности

ax.errorbar(x, y, fmt='s')


#---------------------------/ МНК /--------------------------------

z = np.polyfit(x, y, 1)
print(z)
p = np.poly1d(z)

ax.errorbar(x, p(x), linewidth=2)

#---------------------------//-----------------------------------

plt.show()
