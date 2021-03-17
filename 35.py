from queue import PriorityQueue

que = PriorityQueue()

ans = []

que.put(1)

cnt = 0
pre = None

while cnt <= 1500:
    tmp = que.get()
    if pre == tmp:
        continue
    ans.append(tmp)
    cnt += 1
    que.put(tmp * 2)
    que.put(tmp * 3)
    que.put(tmp * 5)
    pre = tmp

while True:
    a = int(input())
    if a == 0:
        break
    print(ans[a-1])
