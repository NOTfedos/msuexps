arr1 = [380, 340, 301, 260, 221]
arr2 = [339, 301, 260, 221, 184]

arr3 = [356, 311, 280, 241]
arr4 = [311, 280, 241, 199]

s = 0
k = 0

for el1, el2 in zip(arr1, arr2):
    s += abs(el1 - el2)
    k += 1

for el1, el2 in zip(arr3, arr4):
    s += abs(el1 - el2)
    k+=1

print(s / k)