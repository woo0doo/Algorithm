import sys
input = sys.stdin.readline

n = int(input())

color_price_list = []

for _ in range(n):
    color_price_list.append(list(map(int, input().split())))

for i in range(1, n):
    color_price_list[i][0] = min(color_price_list[i-1][1], color_price_list[i-1][2]) + color_price_list[i][0]
    color_price_list[i][1] = min(color_price_list[i-1][0], color_price_list[i-1][2]) + color_price_list[i][1]
    color_price_list[i][2] = min(color_price_list[i-1][0], color_price_list[i-1][1]) + color_price_list[i][2]

print(min(color_price_list[n-1]))
