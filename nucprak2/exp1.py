import matplotlib.pyplot as plt
from template import setup_plot
import csv


a = 0.0059
b = 2.46

fig, ax = plt.subplots()
setup_plot(ax, "Спектр 3 источника", "Энергия, МэВ", "Интенсивность, отн. ед.")


data = csv.reader(open("1 ист Клиентов.txt", "r"), delimiter="\t")
x = []
y = []
cluster = 1
k = 0
buf_x = [0] * cluster
buf_y = [0] * cluster
for row in data:
    buf_x[k] = int(row[0])
    buf_y[k] = int(row[1])
    k += 1
    if (k % cluster) == 0:
        x.append(sum(buf_x) / cluster)
        y.append(sum(buf_y) / cluster)
        k = 0


print(len(x), len(y))
x = list(map(lambda n: a*n+b, x))
ax.plot(x, y, linewidth=3)
plt.show()
