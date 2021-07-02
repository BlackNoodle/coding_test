from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
arr = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)


def bfs(start, arr, visited, k):
    ans = []
    q = deque()
    q.append((start, 0))
    visited[start] = True
    while q:
        point, time = q.popleft()
        if time > k:
            break
        for node in arr[point]:
            if not visited[node]:
                q.append((node, time+1))
                visited[node] = True
                if time+1 == k:
                    ans.append(node)

    return ans

visited = [False for _ in range(n+1)]

ans = bfs(x, arr, visited, k)

if not len(ans):
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)