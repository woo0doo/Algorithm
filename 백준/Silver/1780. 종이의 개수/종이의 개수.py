import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

cnt_zero=0
cnt_minus=0
cnt_plus=0


def solution(x,y,n):
    global cnt_zero,cnt_plus,cnt_minus
    num=graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if (graph[i][j] != num):
                for k in range(3):
                    for l in range(3):
                        solution(x+k*n//3,y+l*n//3,n//3)
                return
    if num == -1:
        cnt_minus +=1
    elif num == 0:
        cnt_zero += 1
    else:
        cnt_plus += 1

solution(0,0,n)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)