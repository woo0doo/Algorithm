n = int(input())

# n1 = 1, n2 = 3, n3 = 5, n4 = 11 n5 = 21 .. dp[i] = dp[i-2]*2 + dp[i-1]

dp = [0 for i in range(1001)]

dp[1], dp[2] = 1,3

for i in range(3,n+1):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[n] % 10007)