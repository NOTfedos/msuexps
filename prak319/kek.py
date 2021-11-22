import matplotlib.pyplot as plt

arr = [380, 356, 340, 311, 301, 280, 260, 241, 221, 199]
x = [1 if x % 2== 0 else -1 for x in range(10)]
print(x)
plt.plot(arr, x, c='red')

arr = [360, 339, 311, 301, 280, 260, 241, 221, 199, 184]
plt.plot(arr, x, c='green')
plt.show()
