import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for j in range(c-b+1):
            if arr[b-1+j] == 0:
                arr[b-1+j] = 1
            else:
                arr[b-1+j] = 0
    elif a == 3:
        for k in range(b-1, c):
            arr[k] = 0
    elif a == 4:
        for t in range(b-1, c):
            arr[t] = 1

for r in arr:
    print(r, end=' ')