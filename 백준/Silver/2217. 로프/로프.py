import sys
input=sys.stdin.readline

n=int(input())

rope=[]
for i in range(n):
    rope.append(int(input()))

rope.sort()
res=0
for i in range(n):
    res=max(res,rope[i]*(len(rope)-i))

print(res)