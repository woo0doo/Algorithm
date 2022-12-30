import sys
#딸기(0) 초코(1) 바나나(2) - > 반복

n=int(input())

a=list(map(int,sys.stdin.readline().split()))
add_n=0
result=0
for i in a:
    if add_n == 2:
        if add_n == i:
            add_n = 0
            result += 1
        
    else: 
        if add_n == i:
            add_n += 1
            result += 1

print(result)