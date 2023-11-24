import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

bnpMoney = n
bnpStock = 0
timingMoney = n
timingStock = 0
timingImproveCnt = 0
timingDecreaseCnt = 0
for i in range(len(arr)):
    bnpStock += bnpMoney // arr[i]
    bnpMoney = bnpMoney % arr[i]

    if i == 0:
        continue
    else:
        if arr[i] > arr[i-1]:
            timingImproveCnt += 1
            timingDecreaseCnt = 0
        elif arr[i] == arr[i-1]:
            timingImproveCnt = 0
            timingDecreaseCnt = 0
        else:
            timingImproveCnt = 0
            timingDecreaseCnt += 1

        if timingImproveCnt >= 3:
            timingMoney += timingStock * arr[i]
            timingStock = 0

        if timingDecreaseCnt >= 3:
            timingStock += timingMoney // arr[i]
            timingMoney = timingMoney % arr[i]


bnpTotalMoney = bnpMoney + arr[-1] * bnpStock
timingTotalMoney = timingMoney + arr[-1] * timingStock

if bnpTotalMoney > timingTotalMoney:
    print("BNP")
elif bnpTotalMoney == timingTotalMoney:
    print("SAMESAME")
else:
    print("TIMING")
