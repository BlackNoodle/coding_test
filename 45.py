t = int(input())

for _ in range(t):
    n = int(input())
    grade = list(map(int, input().split()))
    m = int(input())
    change = []
    for _ in range(m):
        change.append(tuple(map(int, input().split())))

