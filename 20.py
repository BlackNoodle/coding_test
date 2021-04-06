n = int(input())
arr = []
tmp = []

for i in range(n):
    arr.append(list(input().split()))


def check(tmp_arr):
    global n
    kk = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            kk[i][j] = tmp_arr[j][i]
            if tmp_arr[i][j] == "S":
                for k in range(j):
                    if tmp_arr[i][k] == "T":
                        if "O" not in tmp_arr[i][k+1:j]:
                            return "NO"
                for k in range(j+1, n):
                    if tmp_arr[i][k] == "T":
                        if "O" not in tmp_arr[i][j:k]:
                            return "NO"

    for i in range(n):
        for j in range(n):
            if kk[i][j] == "S":
                for k in range(j):
                    if kk[i][k] == "T":
                        if "O" not in kk[i][k+1:j]:
                            return "NO"
                for k in range(j+1, n):
                    if kk[i][k] == "T":
                        if "O" not in kk[i][j:k]:
                            return "NO"


    return "YES"

for i in range(n):
    for j in range(n):
        if arr[i][j] == "X":
            tmp.append([i, j])

cnt = 0

for i in range(len(tmp)-2):
    for j in range(i+1, len(tmp)-1):
        for k in range(j+1, len(tmp)):
            arr[tmp[i][0]][tmp[i][1]] = "O"
            arr[tmp[j][0]][tmp[j][1]] = "O"
            arr[tmp[k][0]][tmp[k][1]] = "O"
            if check(arr) == "YES":
                cnt = 1
                break
            arr[tmp[i][0]][tmp[i][1]] = "X"
            arr[tmp[j][0]][tmp[j][1]] = "X"
            arr[tmp[k][0]][tmp[k][1]] = "X"
        if cnt == 1:
            break
    if cnt == 1:
        break
if cnt == 1:
    print("YES")
else:
    print("NO")
