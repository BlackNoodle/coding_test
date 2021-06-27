def solution(n, build_frame):
    arr = [[-1]*(n+2) for _ in range(n+2)] # -1 기본, 0 기둥, 1 보 , 2 둘다
    answer = []

    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if y == 0 or arr[x-1][y] == 1 or arr[x-1][y] == 2 or arr[x][y-1] == 0 or arr[x][y-1] == 2:
                    if arr[x][y] == -1:
                        arr[x][y] = a
                    else:
                        arr[x][y] = 2
            else:
                if arr[x][y - 1] == 0 or arr[x][y - 1] == 2 or arr[x + 1][y - 1] == 0 or arr[x + 1][y - 1] == 2 or (arr[x-1][y] == 1 and arr[x+1][y] == 1) or (arr[x-1][y] == 2 and arr[x+1][y] == 1) or (arr[x-1][y] == 1 and arr[x+1][y] == 2) or (arr[x-1][y] == 2 and arr[x+1][y] == 2):
                    if arr[x][y] == -1:
                        arr[x][y] = a
                    else:
                        arr[x][y] = 2
        else:
            if a == 0:
                if arr[x][y+1] == -1:
                    if arr[x][y] == 2:
                        arr[x][y] = 1
                    else:
                        arr[x][y] = -1
                elif arr[x][y+1] == -1


    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])) # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])) # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]