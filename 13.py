from itertools import combinations

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

house = []
chi = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chi.append((i, j))

ans = 1e9

for tmp in list(combinations(chi, m)):
    ch_distance = 0
    for h_x, h_y in house:
        house_distance = 1e9
        for x, y in tmp:
            house_distance = min(house_distance, abs(h_x-x)+abs(h_y-y))
        ch_distance += house_distance
    ans = min(ans, ch_distance)

print(ans)