num=int(input())
n=0
while True:
    if num >= n*(n+1)/2 :
        n+=1
    else:
        break
print(n-1)