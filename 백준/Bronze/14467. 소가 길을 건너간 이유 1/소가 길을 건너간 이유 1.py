import sys
input = sys.stdin.readline

n = int(input())
arr = [2] * (n+1)
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if arr[a] == 2:
        arr[a] = b
    elif arr[a] != b:
        cnt += 1
        arr[a] = b
    else:
        continue
print(cnt)