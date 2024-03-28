import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)
cnt = 1
queue = deque()
queue.append(R)

def bfs():
    global cnt
    while queue:
        popleft = queue.popleft()
        if visited[popleft] == 0:
            visited[popleft] = cnt
            cnt += 1
            for i in graph[popleft]:
                queue.append(i)

bfs()
print(*visited[1:], sep='\n')

