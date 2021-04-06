A = input()
B = input()

dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

for i in range(1, len(A) + 1):
    dp[i][0] = dp[i-1][0] + 1

for i in range(1, len(B) + 1):
    dp[0][i] = dp[0][i-1] + 1


for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

print(dp[len(A)][len(B)])