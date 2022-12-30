n=int(input())
result=0
for i in range(n):
    a=input()
    b=int(a[2:])
    if b <=90:
        result+=1
        
print(result)
