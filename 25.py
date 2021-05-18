def solution(N, stages):
    answer = []
    do = [0 for i in range(N + 2)]
    st = [0 for i in range(N + 2)]

    for i in stages:
        for j in range(1, i + 1):
            do[j] += 1
        st[i] += 1

    for i in range(1, N + 1):
        if do[i] != 0:
            answer.append([i, st[i] / do[i]])
        else:
            answer.append([i, 0])

    tmp = sorted(answer, key=lambda t: t[1], reverse=True)

    ans = []

    for i in tmp:
        ans.append(i[0])

    return ans

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))