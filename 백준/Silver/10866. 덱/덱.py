from collections import deque
import sys
n=int(input())
deq=deque()
for i in range(n):
    k=list(sys.stdin.readline().rstrip().split())
    
    if k[0] == "push_front":
        deq.appendleft(k[1])
    elif k[0] == "push_back":
        deq.append(k[1])
    elif k[0] == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif k[0] == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif k[0] == "size":
        print(len(deq))
    elif k[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)
    elif k[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif k[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)