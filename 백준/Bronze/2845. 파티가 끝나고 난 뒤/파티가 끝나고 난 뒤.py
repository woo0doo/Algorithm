l,p=map(int,input().split())

arr1=list(map(int,input().split()))
res=[]
for i in arr1:
    res.append(i-l*p)

print(*res)