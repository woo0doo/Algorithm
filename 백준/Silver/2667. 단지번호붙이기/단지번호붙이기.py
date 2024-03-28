import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

queue = deque()
result = []
def bfs(y, x):
    graph[y][x] = 0
    queue.append((y, x))
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))
                cnt += 1
    result.append(cnt)

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            bfs(y, x)

result.sort()
print(len(result))
print(*result, sep='\n')