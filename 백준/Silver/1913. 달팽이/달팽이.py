# 입력 값이 7일때, 아래로 7 무지성 for문 ?
import sys

n = int(input())
m = int(input())

arr = [[0 for i in range(n)] for _ in range(n)]

cnt = n*n

column = 0
raw = 0

while cnt > 0:
    for i in range(n):
        if arr[i][raw] == 0:
            arr[i][raw] = cnt
            cnt -= 1
            column = i
    for j in range(n):
        if arr[column][j] == 0:
            arr[column][j] = cnt
            cnt -= 1
            raw = j
    for k in range(n-1,-1,-1):
        if arr[k][raw] == 0:
            arr[k][raw] = cnt
            cnt -= 1
            column = k
    for t in range(n-1,-1,-1):
        if arr[column][t] == 0:
            arr[column][t] = cnt
            cnt -= 1
            raw = t

result_column = 0
result_raw = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            result_column = i+1
            result_raw = j+1
        print(arr[i][j], end=' ')
    print()

print(result_column, result_raw)