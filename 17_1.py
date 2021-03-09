from collections import deque

n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

q = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            q.append((arr[i][j], i, j, 0)) # 바이러스 종류, x 위치, y위치, 시간

q.sort()

q = deque(q)

px = [0, 0, 1, -1]
py = [1, -1, 0, -0]

while q:
    vi, x_index, y_index, time = q.popleft()
    if time == s:
        break

    for i in range(4):
        x_tmp = x_index + px[i]
        y_tmp = y_index + py[i]
        if x_tmp < n and y_tmp < n and x_tmp > -1 and y_tmp > -1 and arr[x_tmp][y_tmp] == 0:
            q.append((vi, x_tmp, y_tmp, time+1))
            arr[x_tmp][y_tmp] = vi

print(arr[x-1][y-1])

