import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

heapq.heapify(arr)

ans = 0

while len(arr) > 1:
    tmp1 = heapq.heappop(arr)
    tmp2 = heapq.heappop(arr)
    ans += tmp1
    ans += tmp2
    heapq.heappush(arr, tmp1+tmp2)

print(ans)