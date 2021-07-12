from itertools import permutations


def solution(n, weak, dist):
    l = len(weak)

    for i in range(l):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(l):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[start] + friends[cnt - 1]
            for i in range(start, start + l):
                if weak[i] > pos:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[i] + friends[cnt - 1]
            answer = min(cnt, answer)
    if answer > len(dist):
        return -1
    else:
        return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # 1