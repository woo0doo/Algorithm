import sys
from collections import deque
input=sys.stdin.readline

a,b=map(int,input().split())

arr= deque([i for i in range(1,a+1)])
res=[]
while arr:
    for i in range(b-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())

print("<", end="")
print(*res, sep=", ", end="")
print(">")