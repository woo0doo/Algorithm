n=int(input())

min5=0
min1=0
sec10=0
while n>0:
    if n % 300 ==0:
        min5 += n//5
        break
    elif n%60==0:
        min1=min1+1
        n-=60
    else:
        sec10+=1
        n-=10
if n<0:
    print(-1)
else:
    print(min5,min1,sec10)