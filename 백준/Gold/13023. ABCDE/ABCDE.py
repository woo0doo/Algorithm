n,m=map(int,input().split())
link=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)

ans=0

visited=[False]*n
def dfs(x,depth):
    global ans
    visited[x]=True
    if depth==4:
        ans=True
        return
    for i in link[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i,depth+1)
            visited[i] = False

for i in range(n):
    dfs(i,0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)