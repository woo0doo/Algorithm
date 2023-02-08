import sys
from collections import deque
input=sys.stdin.readline

n,m,r = map(int,input().split())

link=[[] for _ in range(n+1)]
cnt=1

for _ in range(m):
    a,b=map(int,input().split())
    link[a].append(b)
    link[b].append(a)
visited=[0] * (n+1)

for i in range(1,n+1):
    link[i].sort(reverse=True)

queue = deque()
def bfs(x):
    global cnt
    queue.append(x)
    visited[x] = 1
    while queue:
        v=queue.popleft()
        for i in link[v]:
            if visited[i]:
                continue
            cnt += 1
            visited[i] = cnt
            queue.append(i)
bfs(r)
for i in range(1,len(visited)):
    print(visited[i])