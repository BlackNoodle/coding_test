import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    arr.append([name, int(korean), int(english), int(math)])

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])