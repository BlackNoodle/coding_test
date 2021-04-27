n, m = map(int, input().split())
inf = int(1e9)

arr = [[inf]*n for _ in range(n)]
arr2 = [[inf]*n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0
    arr2[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = 1
    arr2[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][k]+arr[k][j], arr[i][j])
            arr2[i][j] = min(arr2[i][k] + arr2[k][j], arr2[i][j])

cnt = 0


for i in range(n):
    tmp = 0
    for j in range(n):
        if arr[i][j] == inf and arr2[i][j] == inf:
            break
        tmp += 1
    if tmp == n:
        cnt += 1

print(arr)

print(cnt)