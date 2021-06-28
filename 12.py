def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove([x, y, a])
            if not complete(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not complete(answer):
                answer.remove([x, y, a])


    return sorted(answer)

def complete(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        else:
            if [x+1, y-1, 0] in answer or [x, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False

    return True

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])) # [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])) # [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]