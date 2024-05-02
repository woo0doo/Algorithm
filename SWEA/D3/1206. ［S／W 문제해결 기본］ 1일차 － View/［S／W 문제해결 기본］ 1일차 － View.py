T = 10

for _ in range(1, T+1):
    N = int(input().rstrip())
    buildings = list(map(int, input().split()))
    sum = 0
    for i in range(len(buildings)):
        if i <= 1:
            height = buildings[i]
            max_diff_building = max(buildings[i + 1], buildings[i + 2])
            if max_diff_building < height:
                sum += height - max_diff_building
        elif len(buildings) -2 <= i:
            if i - len(buildings)-2 == 1:
                height = buildings[i]
                max_diff_building = max(buildings[i - 2], buildings[i - 1], buildings[i + 1])
                if max_diff_building < height:
                    sum += height - max_diff_building
            else:
                height = buildings[i]
                max_diff_building = max(buildings[i - 2], buildings[i - 1])
                if max_diff_building < height:
                    sum += height - max_diff_building
        else:
            height = buildings[i]
            max_diff_building = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
            if max_diff_building < height:
                sum += height - max_diff_building
    print(f'#{_} {sum}')
