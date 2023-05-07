n=int(input())

arr=list(map(int,input().split()))

length=0
cnt=0
for i in arr:
    if length > i:
        pass
    else:
        cnt+=1
    length = i

print(cnt)