import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    deq = deque()
    deq.append(start)
    cnt = 0
    visited = [False] * (n + 1)
    visited[start] = True

    while deq:
        popleft = deq.popleft()
        for next in graph[popleft]:
            if not visited[next]:
                visited[next] = True
                deq.append(next)
                cnt += 1
    return cnt

result = [0] * (n+1)

for i in range(1,n+1):
    cnt = bfs(i)
    result[i] = cnt

max_cnt = max(result)
for j in range(1,n+1):
    if result[j] == max_cnt:
        print(j, end=" ")