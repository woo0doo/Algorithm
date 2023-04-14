from collections import deque
n=int(input())
counts = []
graph=[list(map(int,input())) for _ in range(n)]
def bfs(x,y):

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    queue=deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt+=1
    counts.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
counts.sort()
print(len(counts))
print(*counts, sep="\n")