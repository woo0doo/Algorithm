import sys
input = sys.stdin.readline

test_num = int(input())

for _ in range(test_num):
    n = int(input())

    arr = list(map(int,input().split()))

    dp = [-1000] * (n+1)

    for i in range(len(arr)):
        if i == 0:
            dp[i] = arr[i]
        else:
            dp[i] = max(arr[i], dp[i-1]+arr[i])
    print(max(dp))