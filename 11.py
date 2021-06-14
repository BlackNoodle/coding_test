from collections import deque

N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]

for i in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

L = int(input())
turn = dict()

for _ in range(L):
    a, b = input().split()
    turn[int(a)] = 1 if b == 'D' else -1

ans = 0
snake = [[0, 0]]
location = 0
will_move = deque()
will_move.append(location)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0

while True:
    head_x = snake[0][0]
    head_y = snake[0][1]
    tail_x = snake[-1][0]
    tail_y = snake[-1][1]
    if time in turn:
        location += turn[time]
        location %= 4
    will_move.appendleft(location)
    head_x += dx[location]
    head_y += dy[location]

    if head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or [head_x, head_y] in snake:
        break

    for i in range(len(snake)):
        snake[i][0] += dx[will_move[i]]
        snake[i][1] += dy[will_move[i]]

    if arr[head_x][head_y]:
        arr[head_x][head_y] = 0
        snake.append([tail_x, tail_y])
    else:
        will_move.pop()

    time += 1


print(time+1)
