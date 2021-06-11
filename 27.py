# from collections import Counter
#
# n, x = map(int, input().split())
# arr = list(map(int, input().split()))
#
# count = Counter(arr)
#
# if count[x] == 0:
#     print(-1)
# else:
#     print(count[x])

def binary_serch_start(arr, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == target and (mid == 0 or target > arr[mid-1]):
            return mid
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_serch_end(arr, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == target and (mid == len(arr) - 1 or target < arr[mid+1]):
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, x = map(int, input().split())
arr = list(map(int, input().split()))

start = binary_serch_start(arr, x, 0, n-1)
end = binary_serch_end(arr, x, 0, n-1)

if start == None or end == None:
    print(-1)
else:
    print(end - start + 1)