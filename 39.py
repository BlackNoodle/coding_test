from queue import PriorityQueue

def bfs(arr, visited, n):
    q = PriorityQueue()
    q.put((arr[0][0], (0, 0)))
    visited[0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        tmp = q.get()
        x = tmp[1][0]
        y = tmp[1][1]
        if tmp[1] == (n-1, n-1):
            return tmp[0]
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if 0 <= tmp_x < n and 0 <= tmp_y < n and not visited[tmp_x][tmp_y]:
                q.put((tmp[0]+arr[tmp_x][tmp_y], (tmp_x, tmp_y)))
                visited[tmp_x][tmp_y] = True

t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    visited = [[False]*n for _ in range(n)]
    print(bfs(arr, visited, n))