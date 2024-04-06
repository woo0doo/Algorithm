N = int(input())
plans = [0] * 367

for _ in range(N):
    S, E = map(int, input().split())
    for i in range(E-S+1):
        plans[S+i] += 1

result = 0
temp = 0
day = 0
for i, plan in enumerate(plans):
    if plan == 0 or i == 366:
        result += temp * day
        temp = 0
        day = 0
    else:
        temp = max(temp, plan)
        day += 1
print(result)