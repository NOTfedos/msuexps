arr1 = [7076, 0.028, 0.0196, 7431-6795]
arr2 = [7113, 0.028, 0.0196, 7375-6852]
arr3 = [7132, 0.029, 0.0203, 7413-6870]

for val in range(len(arr1)):
    mean = (arr1[val] + arr2[val] + arr3[val]) / 3
    std = (((arr1[val] - mean)**2 + (arr2[val] - mean)**2 + (arr3[val] - mean)**2) / 6)**0.5
    print(mean, std)