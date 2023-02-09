import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n,m,r = map(int,input().split())

link=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

for j in range(n+1):
    link[j].sort()
visited=[0] * (n+1)

cnt=1

def dfs(x):
    global cnt
    visited[x] = cnt
    for i in link[x]:
        if not visited[i]:
            cnt+=1
            dfs(i)

dfs(r)
print(*visited[1:], sep="\n")