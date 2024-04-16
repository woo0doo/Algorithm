N = int(input())

dp = [0] * 11
for t in range(N):
    idx = int(input())
    for i in range(1, idx + 1):
        if i % 2 == 1:
            dp[i] = dp[i - 1] + i
        else:
            dp[i] = dp[i - 1] - i

    print(f'#{t+1}', dp[idx])
