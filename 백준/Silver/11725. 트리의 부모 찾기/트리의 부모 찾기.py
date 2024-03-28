from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
connect = []
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(n+1)

def bfs():
    while queue:
        popleft = queue.popleft()
        for i in graph[popleft]:
            if ans[i] == 0:
                ans[i] = popleft
                queue.append(i)

bfs()
for an in ans[2:]:
    print(an)