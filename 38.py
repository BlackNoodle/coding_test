n, m = map(int, input().split())
inf = int(1e9)

arr = [[inf]*n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][k]+arr[k][j], arr[i][j])

cnt = 0

for i in range(n):
    tmp = 0
    for j in range(n):
        if arr[i][j] != inf or arr[j][i] != inf:
            tmp += 1
    if tmp == n:
        cnt += 1

print(cnt)