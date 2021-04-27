N = int(input())
K = int(input())
apple = []
for i in range(K):
    apple.append(list(map(int, input().split())))
L = int(input())
location = []

for i in range(L):
    location.append(list(input().split()))

print(location)
