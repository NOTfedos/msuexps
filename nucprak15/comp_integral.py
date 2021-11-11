from math import sqrt


f = open("Klientov.txt")
arr = [0]*1001

start = 186
end = 570

for line in f.readlines():
    ind, amp = list(map(int, line.split()))
    arr[ind] = amp
f.close()

I = 0
sI = 0

for ind in range(start, end):
    I += arr[ind]
    if arr[ind] != 0:
        sI += sqrt(arr[ind])

print(f"I = {I} +- {sI}")
