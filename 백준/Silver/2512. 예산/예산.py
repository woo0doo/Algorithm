import sys
input=sys.stdin.readline
N=int(input())
moneys = list(map(int,input().split()))
available_money = int(input())

total = sum(moneys)
end = max(moneys)
start = 1
if available_money >= total:
    print(end)
else:
    while (end >= start):
        mid = (start+end)//2
        temp_sum = 0
        for money in moneys:
            if money > mid:
                temp_sum += mid
            else:
                temp_sum += money
        if available_money >= temp_sum:
            start = mid + 1
        else:
            end = mid - 1
    print(end)