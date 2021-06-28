n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n-1

ans = -1

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == mid:
        ans = mid
        break
    elif arr[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1


print(ans)