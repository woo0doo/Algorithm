import sys
from collections import deque
input=sys.stdin.readline

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 0
    while queue:
        pop_y, pop_x = queue.popleft()
        for i in range(4):
            ny = pop_y + dy[i]
            nx = pop_x + dx[i]
            if (0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1 and graph[ny][nx] != 0):
                visited[ny][nx] = visited[pop_y][pop_x] + 1
                queue.append((ny, nx))

N, M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

visited = list([-1 for _ in range(M)] for i in range(N))

target_y = 0
target_x = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            target_y = i
            target_x = j
            break
dy = [-1,1,0,0]
dx = [0,0,-1,1]


bfs(target_y, target_x)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
