import sys

n=int(input())
num1=list(map(int,sys.stdin.readline().split()))
n2=int(input())
num2=list(map(int,sys.stdin.readline().split()))

num1.sort()

for i in num2:
    start=0
    end=len(num1)-1
    while start <= end:
        mid = (start+end) // 2
        if i == num1[mid]:
            print(1)
            break
        elif i > num1[mid]:
            start = mid+1
        else:
            end=mid-1
    else:
        print(0)
