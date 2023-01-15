n,l = map(int,input().split())

res=list(map(int,input().split()))

res.sort()
for i in res:
    if i <= l:
        l += 1
    
print(l)