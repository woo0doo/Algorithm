n=input().split('-')

res=[]

for i in n:
    x=0
    k=i.split("+")
    for j in k:
        x+=int(j.lstrip("0"))
    res.append(x)
    
    
print(res[0]*2-sum(res))