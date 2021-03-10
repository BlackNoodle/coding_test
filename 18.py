def solution(p):
    return ar(p)


def ri(s):
    cnt = 0

    for i in s:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return True


def ar(s):
    if s == "":
        return ""

    cnt = 0
    index = None
    for i in range(len(s)):
        if s[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            index = i
            break
    u = s[:i + 1]
    v = s[i + 1:]

    if ri(u):
        return u + ar(v)
    else:
        tmp = ""
        tmp += "("
        tmp += ar(v)
        tmp += ")"
        new_u = ""
        for i in u[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("
        tmp += new_u
        return tmp


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))