res=0
grade=0
for i in range(20):
    a,b,c=map(str,input().split())
    b=float(b)
    if c == "P":
        continue
    grade+=b

    if c == "A+":
        res += 4.5*b
    elif c == "A0":
        res += 4.0*b
    elif c== "B+":
        res += 3.5*b
    elif c== "B0":
        res += 3.0*b
    elif c== "C+":
        res += 2.5*b
    elif c== "C0":
        res += 2.0*b
    elif c== "D+":
        res += 1.5*b
    elif c== "D0":
        res += 1.0*b
    elif c== "F":
        res += 0.0*b

print(res/grade)

