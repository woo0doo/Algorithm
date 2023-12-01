import sys
input = sys.stdin.readline
n = int(input())

arr = []
money = 0
for _ in range(n):
    tip = int(input())
    arr.append(tip)

arr.sort(reverse=True)

for j in range(len(arr)):
    if arr[j] - j <= 0:
        break
    money += arr[j] - j

print(money)