T = int(input())

for t in range(1, T+1):
    N,M,K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    result = True

    dp = [0] * 11112
    for i in range(1,11112):
        if i%M != 0:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + K

    sum = 0
    for i in customer:
        sum += 1
        if dp[i] >= sum:
            continue
        else:
            result = False
            break
    if result == True:
        print(f"#{t} Possible")
    else:
        print(f"#{t} Impossible")
