n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result=0
for i in range(len(b)-1):
    if b[i] <= b[i+1]:
        b[i+1] = b[i]

for i in range(len(a)):
    result+=a[i]*b[i]
print(result)