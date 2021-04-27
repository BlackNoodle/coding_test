s = input()

ans = []
total = 0

for i in range(len(s)):
    if s[i].isdigit():
        total += int(s[i])
    else:
        ans.append(s[i])
ans.sort()
text = "".join(ans)
print(text+str(total))