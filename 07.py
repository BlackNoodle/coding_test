num = input()

l = len(num)
a = num[:l//2]
b = num[l//2:]
sum_a = 0
sum_b = 0

for i in range(len(a)):
    sum_a += int(a[i])
    sum_b += int(b[i])

if sum_a == sum_b:
    print("LUCKY")
else:
    print("READY")