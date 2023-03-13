import sys
input = sys.stdin.readline
n,m=map(int,input().split())


dic=dict()
for i in range(n):
    a,b=map(str,input().rstrip().split())
    dic[a] = b


for i in range(m):
    res=input().rstrip()
    print(dic.get(res))