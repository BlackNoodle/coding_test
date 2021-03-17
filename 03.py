s = input()

cnt = [0, 0]
pre = None

for i in s:
    if i != pre:
        pre = i
        cnt[int(i)] += 1


print(min(cnt))