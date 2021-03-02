n = int(input())

arr = []
ans = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    tmp = 0
    for j in range(5):
        if i - j < 0:
            continue

        if i-j-1 < 0:
            m = 0
        else:
            m = ans[i-j-1]

        if arr[i-j][0] == j+1:
            m += arr[i-j][1]

        tmp = max(m, tmp)
    ans.append(tmp)

print(max(ans))
