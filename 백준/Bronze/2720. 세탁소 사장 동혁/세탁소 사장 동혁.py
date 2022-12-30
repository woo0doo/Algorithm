n=int(input())

for i in range(n):
    num = int(input())
    q=num//25
    num%=25
    d=num//10
    num%=10
    ni=num//5
    num%=5
    print(q,d,ni,num)
