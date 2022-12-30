a,b=map(int,input().split())
result=0
coin=[]
for i in range(a):
    don=int(input())
    if don <= b:
        coin.append(don)
coin.reverse()
for j in range(len(coin)):
    result+=b//coin[j]
    b%=coin[j]
    if b==0:
        break
print(result)
