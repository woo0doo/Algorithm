import math
n=int(input())

arr=list(map(int,input().split()))
cnt=0
for i in arr:
    check=True
    if i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            check = False
            break
    if check == False:
        continue
    else:
        cnt += 1
print(cnt)