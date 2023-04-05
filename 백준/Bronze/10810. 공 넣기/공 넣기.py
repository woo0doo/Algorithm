n,m=map(int,input().split())
res=[0] * (n+1)
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        res[j] = c
print(*res[1:])
