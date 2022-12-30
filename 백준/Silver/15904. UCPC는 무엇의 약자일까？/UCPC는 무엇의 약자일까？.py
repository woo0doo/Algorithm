n=input()
a=n.find("U")

b=0
k=0
while a>=b:
    b=n.find("C",k)
    k+=1
    if b==-1:
        break
c=0
k=b
while b>=c:
    c=n.find("P",k)
    k+=1
    if c==-1:
        break
d=0
k=c
while c>=d:
    d=n.find("C",k)
    k+=1
    if d == -1:
        break
    
if a == -1 or b == -1 or c == -1 or d == -1:
    print("I hate UCPC")
else:
    print("I love UCPC")
