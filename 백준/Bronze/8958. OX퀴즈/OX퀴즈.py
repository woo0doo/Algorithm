import sys

n=int(input())
for i in range(n):
    score=0
    plus=1
    res=list(sys.stdin.readline().rstrip())
    for j in res:
        if j == "O":
            score+=plus
            plus += 1
        else:
            plus = 1
    print(score)
