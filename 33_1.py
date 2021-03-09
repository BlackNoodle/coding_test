n = int(input())

t = []
p = []

for i in range(n):
    t_tmp, p_tmp = map(int, input().split())
    t.append(t_tmp)
    p.append(p_tmp)

dp = [0 for i in range(n+1)]
max_v = 0

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_v)
        max_v = dp[i]
    else:
        dp[i] = max_v


print(max_v)

