arr = []

ans = 0

pos = {}

for i in range(4):
    tmp = list(map(int, input().split()))
    row = []
    for j in range(4):
        row.append([tmp[2*j], tmp[2*j+1]-1])
        pos[tmp[2*j]] = (i, j)
    arr.append(row)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans += arr[0][0][0]
pos[arr[0][0][0]] = (-1, -1)
arr[0][0][0] = -1  # 상어는 -1

def fish(arr, pos):
    for i in range(16):
        if pos[i] == (-1, -1):
            continue
        x = pos[i][0]
        y = pos[i][1]
        nx = x + dx[arr[x][y][1]]
        ny = y + dy[arr[x][y][1]]





