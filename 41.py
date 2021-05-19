n = int(input())
m = int(input())
arr = []

def find_parent(parents, a):
    if parents[a] == a:
        return a
    else:
        return find_parent(parents, parents[a])

def uni(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

parents = [0]*(n+1)

for i in range(n+1):
    parents[i] = i

for i in range(n):
    arr.append(list(map(int, input().split())))

yo = list(map(int, input().split()))


for i in range(n):
    for j in range(i+1, n):
        if arr[i][j] == 1:
            uni(parents, i+1, j+1)


ans = find_parent(parents, yo[0])
kk = "YES"


for i in yo[1:]:
    if ans != find_parent(parents, i):
        kk = "NO"

print(kk)
