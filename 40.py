import heapq

n, m = map(int, input().split())

arr = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

INF = 1e9

release = [False]*(n+1)
dis = [0]*(n+1)

h = []

heapq.heappush(h, (0, 1)) # 거리, 노드번호

ans = [None, -1e9, 0]

while h:
    tmp = heapq.heappop(h)
    if release[tmp[1]]:
        continue
    release[tmp[1]] = True
    dis[tmp[1]] = tmp[0]
    for i in arr[tmp[1]]:
        if not release[i]:
            heapq.heappush(h, (tmp[0]+1, i))

for i in range(1, n+1):
    if dis[i] > ans[1]:
        ans[0] = i
        ans[1] = dis[i]
        ans[2] = 1
    elif dis[i] == ans[1]:
        ans[2] += 1

print(ans[0], ans[1], ans[2])
