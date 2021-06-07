def solution(key, lock):
    m = len(key)
    n = len(lock)

    new_lock = [[0]*n*3 for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for _ in range(4):
        key = rotate_90(key)
        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]


    return False

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def check(lock):
    l = len(lock) // 3

    for i in range(l):
        for j in range(l):
            if lock[l+i][l+j] != 1:
                return False
    return True




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))