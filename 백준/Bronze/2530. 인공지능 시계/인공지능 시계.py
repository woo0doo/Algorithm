a,b,c=map(int,input().split())
d=int(input())
if d < 60:
    if c+d < 60:
        print(a,b,c+d)
    elif c+d >= 60:
        if b+(c+d)//60 < 60:
            print(a,b+(c+d)//60,(c+d)%60)
        elif b+(c+d)//60 >= 60:
            if a+(b+(c+d)//60)//60 < 24:
                print(a+(b+(c+d)//60)//60,(b+(c+d)//60)%60,(c+d)%60)
            elif a+(b+(c+d)//60)//60 >= 24:
                print((a+(b+(c+d)//60)//60)%24,(b+(c+d)//60)%60,(c+d)%60)
else:
    if b+(c+d)//60 < 60:
        print(a,b+(c+d)//60,(c+d)%60)
    elif b+(c+d)//60 >= 60:
        if a+(b+(c+d)//60)//60 < 24:
            print(a+(b+(c+d)//60)//60,(b+(c+d)//60)%60,(c+d)%60)
        elif a+(b+(c+d)//60)//60 >= 24:
            print((a+(b+(c+d)//60)//60)%24,(b+(c+d)//60)%60,(c+d)%60)
    