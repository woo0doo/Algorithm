cash=int(input())

arr=list(map(int,input().split()))
junMoney=cash
junCnt=0
sungMoney=cash
sungCnt=0
for i in arr:
    junCnt += junMoney//i
    junMoney %= i

plusCnt=0
minusCnt=0
for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        minusCnt=0
        plusCnt+=1
    elif arr[i] < arr[i-1]:
        plusCnt=0
        minusCnt+=1

    if plusCnt >= 3:
        sungMoney+=arr[i]*sungCnt
        sungCnt=0
    elif minusCnt >= 3:
        sungCnt+=sungMoney//arr[i]
        sungMoney%=arr[i]

j = junMoney + junCnt * arr[-1]
s = sungMoney + sungCnt * arr[-1]

if j>s:
    print("BNP")
elif j<s:
    print("TIMING")
else:
    print("SAMESAME")