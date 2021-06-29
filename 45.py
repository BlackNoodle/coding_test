from collections import deque
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    grade = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    graph = [[] for i in range(n+1)]
    cnt = [0 for i in range(n+1)]

    for i in range(len(grade)-1):
        for j in range(i+1, len(grade)):
            graph[grade[i]].append(grade[j])
            cnt[grade[j]] += 1

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            cnt[a] += 1
            cnt[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            cnt[b] += 1
            cnt[a] -= 1

    q = deque()
    for i in range(1, n+1):
        if cnt[i] == 0:
            q.append(i)
    ans = []

    while q:
        if len(q) != 1:
            ans = "?"
            break
        tmp = q.popleft()
        ans.append(tmp)
        for i in graph[tmp]:
            cnt[i] -= 1
            if cnt[i] == 0:
                q.append(i)

    if ans == "?":
        print(ans)
    elif len(ans) != n:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, ans)))
