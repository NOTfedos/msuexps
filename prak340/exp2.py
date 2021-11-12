import matplotlib.pyplot as plt
from template import setup_plot


fig, ax = plt.subplots()
setup_plot(ax, r"График зависимости напряжения на детекторе $U$ от угла рупора $\phi$",
           r"$\phi$, $^{\circ}$", r"$U$, $В$")

x = [0, 5, 10, 15, 20, 25, 30, 35, 40]
y = list(map(lambda k: k*2, [6.4, 6, 5.4, 4.7, 4, 3.7, 3.6, 3.6, 3.6]))

x_arr = [0.1]*9
y_arr = [0.2]*9

ax.errorbar(x, y, x_arr, y_arr, fmt='s')
plt.show()
