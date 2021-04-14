from collections import deque

n, l, r = map(int, input().split())

arr = list()

for _ in range(n):
    arr.append(list(map(int, input().split())))


def bfs(visited, i, j):
    global n, l, r

    q = deque()
    q.append((i, j))
    visited[i][j] = True

    union = []
    s = 0

    while q:
        start = q.popleft()
        union.append(start)
        i = start[0]
        j = start[1]
        s += arr[i][j]

        if i - 1 >= 0 and l <= abs(arr[i-1][j] - arr[i][j]) <= r and not visited[i-1][j]:
            q.append((i-1, j))
            visited[i-1][j] = True
        if j - 1 >= 0 and l <= abs(arr[i][j-1] - arr[i][j]) <= r and not visited[i][j-1]:
            q.append((i, j-1))
            visited[i][j-1] = True
        if i + 1 < n and l <= abs(arr[i+1][j] - arr[i][j]) <= r and not visited[i+1][j]:
            q.append((i+1, j))
            visited[i+1][j] = True
        if j + 1 < n and l <= abs(arr[i][j+1] - arr[i][j]) <= r and not visited[i][j+1]:
            q.append((i, j+1))
            visited[i][j+1] = True

    val = s//len(union)

    for tmp in union:
        arr[tmp[0]][tmp[1]] = val

cnt = 0

def bfs_need(visited, i, j):
    if i - 1 >= 0 and l <= abs(arr[i - 1][j] - arr[i][j]) <= r and not visited[i - 1][j]:
        return True
    if j - 1 >= 0 and l <= abs(arr[i][j - 1] - arr[i][j]) <= r and not visited[i][j - 1]:
        return True
    if i + 1 < n and l <= abs(arr[i + 1][j] - arr[i][j]) <= r and not visited[i + 1][j]:
        return True
    if j + 1 < n and l <= abs(arr[i][j + 1] - arr[i][j]) <= r and not visited[i][j + 1]:
        return True

    return False


while True:
    visited = [[False]*n for i in range(n)]
    uu = True
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs_need(visited, i, j):
                    bfs(visited, i, j)
                else:
                    visited[i][j] = True
            else:
                uu = False

    if uu:
        break

    cnt += 1

print(cnt)