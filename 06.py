from queue import PriorityQueue

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    q = PriorityQueue()

    for i in range(len(food_times)):
        q.put((food_times[i], i+1))

    cnt = 0

    while not q.empty():
        tmp = q.get()
        if (tmp[0] - cnt)*(q.qsize()+1) < k:
            k -= (tmp[0] - cnt)*(q.qsize()+1)
            cnt = tmp[0]
            continue
        li = [tmp[1]]
        while not q.empty():
            li.append(q.get()[1])
        li.sort()

        return li[k%len(li)]

    return answer


print(solution([3, 1, 2], 5))
print(solution([4,2,3,6,7,1,5,8], 16))
print(solution([4,2,3,6,7,1,5,8], 27))