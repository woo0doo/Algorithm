from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    err=0
    p=input()
    n=int(input())
    arr=deque(input().rstrip()[1:-1].split(","))
    cnt=0
    if n == 0:
        arr=deque([])

    for i in range(len(p)):
        if p[i] == "R":
            cnt += 1
        elif p[i] == "D":
            if cnt % 2 == 0:
                if arr:
                    arr.popleft()
                else:
                    print("error")
                    err=1
                    break
            else:
                if arr:
                    arr.pop()
                else:
                    print("error")
                    err=1
                    break
    if err==0:
        if cnt % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")