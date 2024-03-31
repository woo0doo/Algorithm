import sys
input = sys.stdin.readline

N, M = map(int,input().split())
woods = list(map(int, input().split()))

start = 1
end = max(woods)
while (end >= start):
    mid = (start + end) // 2
    temp_height = 0
    for i in woods:
        if mid - i >= 0:
            continue
        else:
            temp_height += i - mid
    if temp_height >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)