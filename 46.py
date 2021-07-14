from collections import deque

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 9:
            position = (i, j)
            arr[i][j] = 0

size = 2
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    dis = [[-1]*n for _ in range(n)]
    q = deque()
    q.append(position)
    dis[position[0]][position[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= size and dis[nx][ny] == -1:
                q.append((nx, ny))
                dis[nx][ny] = dis[x][y] + 1

    return dis

def find_fish(dis):
    po = None
    time = 1e9
    for i in range(n):
        for j in range(n):
            if 0 < dis[i][j] < time and 1 <= arr[i][j] < size:
                time = dis[i][j]
                po = (i, j)

    return po, time

cnt = 0
ans = 0

while True:
    dis = bfs()
    position, time = find_fish(dis)
    if not position:
        break
    cnt += 1
    arr[position[0]][position[1]] = 0
    if cnt == size:
        cnt = 0
        size += 1
    ans += time

print(ans)