n=int(input())

res=[1,0,0]


for i in range(n):
    a,b=map(int,input().split())
    temp=res[a-1]
    res[a-1]=res[b-1]
    res[b-1]=temp

print(res.index(1)+1)