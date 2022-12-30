import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
result=[]
a.sort()
for i in range(n):
    min_1=a.pop(0)
    max_1=a.pop()
    add=min_1+max_1
    result.append(add)
print(min(result))