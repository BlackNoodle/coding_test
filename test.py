from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    start = n

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if dif_one(words[i], words[j]):
                graph[i][j] = 1
                graph[j][i] = 1

    for i in range(n):
        if words[i] == target:
            end = i
        if dif_one(begin, words[i]):
            graph[i][n] = 1
            graph[n][i] = 1

    visited = [0] * (n + 1)

    return bfs(start, visited, graph, end)


def dif_one(word1, word2):
    cnt = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
        if cnt >= 2:
            return False

    return True


def bfs(start, visited, graph, end):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        tmp, time = q.popleft()
        if tmp == end:
            return time
        for i in range(len(graph[tmp])):
            if graph[tmp][i] == 1 and not visited[i]:
                q.append((i, time + 1))
                visited[i] = 1

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))