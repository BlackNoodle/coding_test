s = input()

answer = 0

for i in s:
    tmp = int(i)
    if tmp <= 1 or answer <= 1:
        answer += tmp
    else:
        answer *= tmp


print(answer)

