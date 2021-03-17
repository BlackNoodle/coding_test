n = int(input())
arr = list(map(int, input().split()))
th = list(map(int, input().split()))

yo = []

# 0 더하기 1 빼기 2 곱하기 3 나누기

for i in range(len(th)):
    for j in range(th[i]):
        yo.append(i)


from itertools import permutations

tmp = list(permutations(yo, len(yo)))
tmp = set(tmp)

ma = -100000000
mi = 1000000000


for i in tmp:
    v = arr[0]
    for k in range(len(i)):
        if i[k] == 0:
            v += arr[k+1]
        elif i[k] == 1:
            v -= arr[k+1]
        elif i[k] == 2:
            v *= arr[k+1]
        else:
            if v < 0:
                v = (-v) // arr[k+1]
                v = -v
            else:
                v = v // arr[k+1]

    ma = max(v, ma)
    mi = min(v, mi)

print(ma)
print(mi)