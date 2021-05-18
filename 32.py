n = int(input())
arr = []
dp = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    dp.append([0]*len(tmp))

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        num = 0
        if j < len(arr[i-1]):
            num = max(num, arr[i][j] + dp[i-1][j])
        if j-1 >= 0:
            num = max(num, arr[i][j] + dp[i-1][j-1])
        dp[i][j] = num

print(max(dp[-1]))