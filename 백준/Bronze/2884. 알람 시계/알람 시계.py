h,m = map(int,input().split())
if m<45:
    if h==0:
        h=23
        a=m-45
        m=60+a
        print(h,m)
    else:
        h-=1
        a=m-45
        m=60+a
        print(h,m)
else:
    m-=45
    print(h,m)
