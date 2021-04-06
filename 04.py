n = int(input())
arr = list(map(int, input().split()))

arr.sort()

target = 1

for i in arr:
    if target >= i:
        target += i
    else:
        break

print(target)