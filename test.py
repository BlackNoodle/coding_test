n, m, x = map(int, input().split())
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

u = 0
v = 0

for i in range(n):
    if arr[i][x-1] == inf:
        u += 1
    if arr[x-1][i] == inf:
        v += 1

print(n - u, v + 1)
