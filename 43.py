import sys

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    arr = []

    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        arr.append((c, a, b))
    arr.sort()
    parent = [i for i in range(m)]
    total = 0

    for tmp in arr:
        z, x, y = tmp
        if find_parent(parent, x) != find_parent(parent, y):
            union(parent, x, y)
        else:
            total += z

    print(total)
