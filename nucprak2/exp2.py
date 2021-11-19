import csv
from math import log, e


data = csv.reader(open("Ra=226 Клиентов.txt", "r"), delimiter="\t")
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

print(len(x), len(y), x[len(x)-1])
A1 = 0
for i in range(274, 418):
    A1 += y[i]

A2 = 0
for i in range(418, 483):
    A2 += y[i]
A2 *= 2

print(A1, A2)

print(log(A1 / (A1 - A2), e) / log(2, e) * 22.3)
