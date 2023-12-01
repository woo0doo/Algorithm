import sys
input = sys.stdin.readline
n = int(input())

arr = []
money = 0
for _ in range(n):
    price = int(input())
    arr.append(price)

arr.sort(reverse=True)

for j in range(len(arr)):
    if j % 3 == 2:
        continue
    money += arr[j]

print(money)