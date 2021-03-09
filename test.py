n, m = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0
cnt = 0

while i < len(a) and j < len(a):
    if sum(a[i:j+1]) < m:
        j += 1
    elif sum(a[i:j+1]) == m:
        cnt += 1
        i += 1
    else:
        i += 1

print(cnt)