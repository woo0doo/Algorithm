import sys
input = sys.stdin.readline
n = int(input())

arr = [[0] * _ for _ in range(1,n+1)]
arr[0][0] = int(input())

for i in range(1,n):
    numbers = list(map(int, input().split()))
    for j in range(len(numbers)):
        if j == 0:
            arr[i][j] = arr[i-1][j] + numbers[j]
        elif j == len(numbers)-1:
            arr[i][j] = arr[i-1][j-1] + numbers[j]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + numbers[j]

print(max(arr[n-1]))