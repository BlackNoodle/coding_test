def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        pre = ""
        ans = ""
        cnt = 1
        idx = 0
        for j in range(0, len(s), i):
            string = s[j:j + i]
            if string == pre:
                cnt += 1
            else:
                if cnt != 1:
                    ans += str(cnt)
                ans += pre
                pre = string
                cnt = 1
            idx = j + i
        if cnt != 1:
            ans += str(cnt)
        ans += pre
        ans += s[idx:]

        answer = min(answer, len(ans))

    return answer
