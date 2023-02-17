import sys
sys.setrecursionlimit(10*9)


t=int(input())

def solution(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return solution(x-1) + solution(x-2) + solution(x-3)



for i in range(t):
    n=int(input())
    print(solution(n))
