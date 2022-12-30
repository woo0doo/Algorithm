a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
result=0
if a>x:
    result+=x               ## 치킨먹고픈 사람이 쿠폰보다 많을 때
    a=a-x
    x=0
elif a<=x:                  ## 치킨<=쿠폰
    result+=a
    x=x-a
    a=0
    y+=x//3                 ## 남은쿠폰 y에 +
    x=0
    
if b>y:                     ## 피자>쿠폰
    result+=y
    b=b-y
    y=0
elif b<=y:                  ## 피자<=쿠폰
    result+=b
    y=y-b
    b=0
    z+=y//3                 ## 남은쿠폰 z에 +
    y=0

if c>z:                     ## 햄버거>쿠폰
    result+=z
    c=c-z
    z=0
elif c<=z:                  ## 햄버거<=쿠폰
    result+=c
    z=z-c
    c=0
    x=z//3                  ## 남은 쿠폰 x에 +
    z=0

if x>=a:
    result+=a
    x=x-a
    y+=x//3
    if b!=0:
        if y>=b:
            result+=b
        else:
            result+=y
    
elif x<a:
    result+=x


print(result)
