t = int(input())
for _ in range(t):
    ans = -1
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[-1]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = arr[i*m]

    tmp = [-1, 0, 1]

    for j in range(m-1):
        for i in range(n):
            max_value = -1
            for k in range(3):
                n_i = i+tmp[k]
                if 0 <= n_i < n:
                    max_value = max(max_value, dp[n_i][j])
            dp[i][j+1] = max_value + arr[i*m+j+1]
            ans = max(ans, dp[i][j+1])

    print(ans)
