from collections import deque
from itertools import combinations

n, m = map(int, input().split())
arr = []

can_wall = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            can_wall.append((i, j))

def bfs(arr, n, m):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    safe = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
                safe += 1
            elif arr[i][j] == 0:
                safe += 1

    size = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        size += 1
        x, y = q.popleft()
        for i in range(4):
            d_x = x + dx[i]
            d_y = y + dy[i]
            if 0 <= d_x < n and 0 <= d_y < m and arr[d_x][d_y] == 0 and not visited[d_x][d_y]:
                q.append((d_x, d_y))
                visited[d_x][d_y] = 1

    return safe - size

ans = -1

for x, y, z in list(combinations(can_wall, 3)):
    arr[x[0]][x[1]] = 1
    arr[y[0]][y[1]] = 1
    arr[z[0]][z[1]] = 1
    ans = max(ans, bfs(arr, n, m))
    arr[x[0]][x[1]] = 0
    arr[y[0]][y[1]] = 0
    arr[z[0]][z[1]] = 0

print(ans)

