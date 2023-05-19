import sys
input=sys.stdin.readline

n,k=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))


for i in range(k):
    tem=[0] * n
    for j in range(n):
        tem[arr2[j]-1]=arr1[j]
    arr1 = tem
print(*arr1)