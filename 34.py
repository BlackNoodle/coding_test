n = int(input())

arr = list(map(int, input().split()))

dp = []

for i in range(len(arr)):
    m = 1
    for j in range(i):
        if arr[i] < arr[j]:
            tmp = dp[j] + 1
            m = max(m, tmp)
    dp.append(m)

print(n - max(dp))