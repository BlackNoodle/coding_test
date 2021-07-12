def solution(words, queries):
    answer = []
    real = [[] for i in range(10001)]
    real_reverse = [[] for i in range(10001)]

    for word in words:
        real[len(word)].append(word)
        real_reverse[len(word)].append(word[::-1])

    for i in range(10001):
        real[i].sort()
        real_reverse[i].sort()

    for query in queries:
        q_s = query.replace("?", "a")
        q_e = query.replace("?", "z")
        cnt = 0
        if query[0] == "?":
            word_list = real_reverse[len(query)]
            q_s = q_s[::-1]
            q_e = q_e[::-1]
        else:
            word_list = real[len(query)]

        s = bsearch(word_list, q_s, 0, len(word_list)-1)
        e = bsearch(word_list, q_e, 0, len(word_list) - 1)

        answer.append(e-s)

    return answer

def bsearch(arr, word, start, end):
    if start > end:
        return start

    mid = (start+end)//2

    if arr[mid] < word:
        return bsearch(arr, word, mid+1, end)
    else:
        return bsearch(arr, word, start, mid-1)


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))