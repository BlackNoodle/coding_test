import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:

        a = heapq.heappop(scoville)
        if len(scoville) > 0:
            b = heapq.heappop(scoville)
        else:
            answer = -1
            break
        answer += 1
        heapq.heappush(scoville, a + 2 * b)

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))