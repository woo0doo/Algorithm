n,m=map(int,input().split())

arr=[i for i in range(1,n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    a,b,c=a-1,b-1,c-1
    arr = arr[:a]+arr[c:b+1]+arr[a:c]+arr[b+1:]
    
print(*arr)