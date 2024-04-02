graph = []
for _ in range(9):
    graph.append(list(map(int, input().split())))

def row(a, n):
    for i in range(9):
        if n == graph[a][i]:
            return False
    return True

def column(a, n):
    for i in range(9):
        if n == graph[i][a]:
            return False
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if n == graph[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True

def find(n):
    if n == len(blank):
        for i in graph:
            print(*i)
        exit()

    for i in range(1, 10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            graph[y][x] = i
            find(n+1)
            graph[y][x] = 0

blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i,j])
find(0)