arr1 = [381, 342, 303, 264, 226, 187, 149]
arr2 = [398, 361, 321, 283, 246, 205, 166]

s = 0

for i in range(1, 6):
    s += 2*abs(arr1[i-1] - arr1[i])
    s += 2*abs(arr2[i-1] - arr2[i])

print(s / 12 / 1000)

print(3e8 / 3.850 / 1e9)
