# n1=1, n2=2, n3=3, n4=5 n5 = 8 피보나치?
# 이거 왜 메모리 초과? ㄷㄷ
# 15746으로 나누면 수가 반복되나보다.. 아니네
# 숫자를 나누어서 넣을까?


n=int(input())

dp = [0] * 1_000_001

for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746


print(dp[n])
