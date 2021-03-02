n, k = map(int, input().split())
arr = []

ans = [4000 for i in range(k+1)]

for i in range(n):
    arr.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        leng = abs((x-1) - i) + abs((y-1) - j)
        if arr[i][j] != 0:
            ans[arr[i][j]] = min(leng, ans[arr[i][j]])


if min(ans) <= s:
    for i in range(len(ans)):
        if min(ans) == ans[i]:
            print(i)
            break
else:
    print(0)