from collections import deque

def solution(maps):
    queue = deque()
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue.append((0,0))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < len(maps) and 0 <= cx < len(maps[0]) and maps[cy][cx] == 1:
                maps[cy][cx] = maps[y][x] + 1
                queue.append((cy, cx))
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    if answer == 1:
        return -1
    return answer