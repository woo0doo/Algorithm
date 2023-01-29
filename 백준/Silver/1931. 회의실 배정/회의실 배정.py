import sys
input=sys.stdin.readline

n=int(input())
con=[]
for _ in range(n):
    a=list(map(int,input().split()))
    con.append(a)

con.sort(key=lambda x:x[0])
con.sort(key=lambda x:x[1])

last=0
cnt=0

for i,j in con:
    if i >= last:
        cnt += 1
        last = j
print(cnt)