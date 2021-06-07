from sys import stdin

G = int(stdin.readline())
P = int(stdin.readline())

parent = [i for i in range(G+1)]


def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def uni(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

result = 0

for _ in range(P):
    par = find_parent(parent, int(stdin.readline()))
    if par == 0:
        break
    uni(parent, par, par - 1)
    result += 1

print(result)
