from queue import PriorityQueue


def solution(scoville, K):
    answer = 0
    q = PriorityQueue()

    for i in scoville:
        q.put(i)

    ans = False

    while q.qsize() > 1:
        tmp1 = q.get()
        tmp2 = q.get()

        if tmp1 >= K:
            ans = True
            break
        q.put(tmp1 + 2 * tmp2)
        answer += 1

    if ans:
        return answer
    else:
        return -1


print(solution([1, 2, 3, 9, 10, 12], 7))