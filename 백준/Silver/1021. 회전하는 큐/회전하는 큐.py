from collections import deque

deq=deque()

n,m=map(int,input().split())

for i in range(n):
    deq.append(i+1)

cnt = 0
num = list(map(int,input().split()))
for i in num:
    if deq[0] == i:
        deq.popleft()
    elif deq.index(i) <= (len(deq) - deq.index(i)):
        for j in range(deq.index(i)):
            deq.append(deq.popleft())
            cnt += 1
        if deq[0] == i:
            deq.popleft()
    elif deq.index(i) > (len(deq) - deq.index(i)):
        for k in range(len(deq) - deq.index(i)):
            deq.appendleft(deq.pop())
            cnt += 1
        if deq[0] == i:
            deq.popleft()

print(cnt)