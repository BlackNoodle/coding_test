n, m = map(int, input().split())
arr = list(map(int, input().split()))

total = int((n*(n-1))/2)

di = dict()

for i in range(1, m+1):
    di[i] = 0

for i in arr:
    di[i] += 1

for k in di.keys():
    total -= int((di[k]*(di[k]-1))/2)

print(total)

