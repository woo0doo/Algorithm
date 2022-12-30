import sys
a,b=map(int,sys.stdin.readline().split())
c=[]
result = 0
for i in range(a):
    c.append(sys.stdin.readline())
for j in range(b):
    k = sys.stdin.readline()
    if k in c:
        result+=1
print(result)