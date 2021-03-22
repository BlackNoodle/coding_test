n = int(input())

arr = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, current):
    global min_val, max_val, plus, minus, mul, div

    if i == n:
        min_val = min(current, min_val)
        max_val = max(current, max_val)
    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, current+arr[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, current-arr[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, current*arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(current/arr[i]))
            div += 1


dfs(1, arr[0])

print(max_val)
print(min_val)
