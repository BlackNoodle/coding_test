n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]

ans = 0

while start <= end:
    mid = (start+end) // 2

    tmp = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= mid + tmp:
            cnt += 1
            tmp = arr[i]

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
