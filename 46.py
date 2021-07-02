from collections import deque
import sys

n = int(sys.stdin.readline())
arr = []
position = None

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if arr[i][j] == 9:
            position = (i, j)

state = 2
cnt = 0

def bfs(visited, start, n, state, purpose):
    q = deque()
    q.append((start, 0))
    find = False
    time = None
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        po, t = q.popleft()
        x, y = po
        if (x, y) == purpose:
            find = True
            time = t
            break
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <= cy < n and not visited[cx][cy] and arr[cx][cy] <= state:
                q.append(((cx, cy), t + 1))
                visited[cx][cy] = 1

    if find:
        return time
    else:
        return 0

def can_eat(state, n):
    ok = []
    for i in range(n):
        for j in range(n):
            if 1 <= arr[i][j] <= 6 and arr[i][j] < state:
                ok.append((i, j))
    return ok

ans = 0

while True:
    can = can_eat(state, n)
    if not can:
        break

    min_time = 1e9
    min_fed = None

    for tmp in can:
        visited = [[0]*n for _ in range(n)]
        time = bfs(visited, position, n, state, tmp)
        if time != 0:
            if time < min_time:
                min_time = time
                min_fed = tmp

    if min_fed == None:
        break

    arr[min_fed[0]][min_fed[1]] = 9
    arr[position[0]][position[1]] = 0
    position = min_fed
    ans += min_time
    cnt += 1
    if cnt == state:
        state += 1
        cnt = 0

print(ans)