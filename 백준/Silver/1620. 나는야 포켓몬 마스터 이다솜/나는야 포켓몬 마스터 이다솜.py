import sys
input=sys.stdin.readline
a=[]
N,M=map(int,input().split())
for i in range(N):
    a.append(input().replace("\n", ""))
for _ in range(M):
    b=input().replace("\n", "")
    try:
        b=int(b)
        print(a[b-1])
    except ValueError:
        b=str(b)
        print((a.index(b))+1)
