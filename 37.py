n = int(input())
m = int(input())
INF = 987654321

arr = [[INF]*n for j in range(n)]

for _ in range(m):
    i, j, c = map(int, input().split())
    if arr[i-1][j-1] > c:
        arr[i-1][j-1] = c

for i in range(n):
    arr[i][i] = 0

for m in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            arr[i][j] = min(arr[i][j], arr[i][m]+arr[m][j])


for i in arr:
    for j in i:
        if j == INF:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()