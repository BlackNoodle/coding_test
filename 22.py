from collections import deque

def solution(board):
    n = len(board)
    visited = {}

    for i in range(n-1):
        for j in range(n):
            visited[(float(i)+0.5, float(j))] = False
            visited[(float(j), float(i) + 0.5)] = False

    answer = bfs(board, visited, (0.0, 0.5), n)

    return answer

def bfs(board, visited, start, n):
    q = deque()
    q.append([start, 0])
    visited[start] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ddx = [0.5, -0.5, 0.5, -0.5]
    ddy = [-0.5, -0.5, 0.5, 0.5]

    ch_ga_x = [1, -1, 1, -1]
    ch_ga_y = [0.5, 0.5, -0.5, -0.5]
    ch_se_x = [-0.5, 0.5, -0.5, 0.5]
    ch_se_y = [-1, -1, 1, 1]

    while q:
        tmp = q.popleft()
        node = tmp[0]
        time = tmp[1]

        if node == (float(n-1.5), float(n-1)) or node == (float(n-1), float(n-1.5)):
            return time

        for i in range(4):
            new_node = (node[0] + dx[i], node[1] + dy[i])

            if 0 <= new_node[0] <= n-1 and 0 <= new_node[1] <= n-1:
                if check(board, new_node) and not visited[new_node]:
                    q.append([new_node, time+1])
                    visited[new_node] = True

        for i in range(4):
            new_node = (node[0] + ddx[i], node[1] + ddy[i])
            if node[0] == int(node[0]):
                ch_x = int(node[0] + ch_ga_x[i])
                ch_y = int(node[1] + ch_ga_y[i])
            else:
                ch_x = int(node[0] + ch_se_x[i])
                ch_y = int(node[1] + ch_se_y[i])


            if 0 <= new_node[0] <= n-1 and 0 <= new_node[1] <= n-1 and 0 <= ch_x < n and 0 <= ch_y < n:
                if check(board, new_node) and not visited[new_node] and board[ch_x][ch_y] == 0:
                    q.append([new_node, time+1])
                    visited[new_node] = True

def check(board, node):
    x = node[0]
    y = node[1]

    if x == int(x):
        x1 = int(x)
        x2 = int(x)
        y1 = int(y-0.5)
        y2 = int(y+0.5)
    else:
        x1 = int(x-0.5)
        x2 = int(x+0.5)
        y1 = int(y)
        y2 = int(y)

    if board[x1][y1] == 0 and board[x2][y2] == 0:
        return True
    else:
        return False

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]])) # 21
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]])) # 11
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])) # 33