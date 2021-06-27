import sys

n = int(sys.stdin.readline())
x = []
y = []
z = []
weight = []

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    weight.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    weight.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    weight.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

weight.sort()

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])

    return parents[x]

def union_graph(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

parents = [i for i in range(n)]

total = 0

for cost, x, y in weight:
    if find_parent(parents, x) != find_parent(parents, y):
        total += cost
        union_graph(parents, x, y)

print(total)
