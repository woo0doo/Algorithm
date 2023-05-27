n1=int(input())
n2=int(input())
n3=int(input())

if n1+n2+n3==180:
    if n1==n2==n3:
        print("Equilateral")
    elif n1==n2 or n2==n3 or n3==n1:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")