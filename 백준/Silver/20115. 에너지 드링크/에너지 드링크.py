import sys
input = sys.stdin.readline
n = int(input())

drink_list = list(map(int, input().split()))
drink_list.sort(reverse=True)
max_drink = drink_list[0]

for j in range(1, len(drink_list)):
    max_drink += drink_list[j] / 2

print(max_drink)