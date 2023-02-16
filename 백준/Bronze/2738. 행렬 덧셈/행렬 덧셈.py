a,b=map(int,input().split())

arr1=[list(map(int,input().split())) for _ in range(a)]
arr2=[list(map(int,input().split())) for _ in range(a)]

result=[]
for i in range(a):
    for j in range(b):
        print(arr1[i][j] + arr2[i][j], end=' ')
    print()

