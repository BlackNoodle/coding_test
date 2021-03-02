n = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = -1

ans = 0

for i in range(len(arr)):
    if i-s >= arr[i]:
        ans += 1
        s = i


print(ans)
