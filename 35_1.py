n = int(input())

arr = [0] * n

arr[0] = 1

idx2 = idx3 = idx5 = 0

num2 = 2
num3 = 3
num5 = 5

for i in range(1, n):
    arr[i] = min(num2, num3, num5)

    if arr[i] == num2:
        idx2 += 1
        num2 = arr[idx2] * 2
    if arr[i] == num3:
        idx3 += 1
        num3 = arr[idx3] * 3
    if arr[i] == num5:
        idx5 += 1
        num5 = arr[idx5] * 5

print(arr[-1])
