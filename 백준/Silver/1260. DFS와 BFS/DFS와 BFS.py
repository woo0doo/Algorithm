from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(r):
    q = deque([r])
    visited2[r] = True
    while q:
        r = q.popleft()
        print(r,end=' ')
        for i in range(1,n+1):
            if not visited2[i] and graph[r][i]:
                q.append(i)
                visited2[i] = True

def dfs(r):
    visited1[r] = True
    print(r,end=' ')
    for i in range(1,n+1):
        if not visited1[i] and graph[r][i]:
            dfs(i)

dfs(r)
print()
bfs(r)