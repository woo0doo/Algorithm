import sys
input=sys.stdin.readline

com=int(input())
net=int(input())

link=[[] for _ in range(com+1)]

for i in range(net):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

cnt=0
visit = [False] * (com + 1)
def dfs(x):
    global cnt
    visit[x] = True
    for i in link[x]:
        if visit[i] == False:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)