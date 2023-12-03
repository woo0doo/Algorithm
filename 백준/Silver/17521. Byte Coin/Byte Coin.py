import sys

input = sys.stdin.readline

n, money = map(int, input().split())
arr = []
for _ in range(n):
    s = int(input())
    arr.append(s)
coin = 0

def find_last_sell_index():
    for j in range(n, 1, -1):
        if arr[j - 1] > arr[j - 2]:
            return j - 1


idx = find_last_sell_index()

for i in range(n):
    if i == idx:
        money += coin * arr[i]
        coin = 0
        break
    if i == n - 1:
        money += coin * arr[i]
        coin = 0
    elif arr[i] < arr[i + 1]:
        coin += money // arr[i]
        money %= arr[i]
    elif arr[i] > arr[i + 1]:
        money += coin * arr[i]
        coin = 0


print(money)
