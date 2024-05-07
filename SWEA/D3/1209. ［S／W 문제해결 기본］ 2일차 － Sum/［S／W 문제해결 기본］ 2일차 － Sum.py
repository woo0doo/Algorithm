T = 10

for _ in range(1, T+1):
    t = int(input())
    bingo = []
    max_num = 0
    for i in range(100):    # 가로
        arr = list(map(int, input().split()))
        arr_max = sum(arr)
        if arr_max > max_num:
            max_num = arr_max
        bingo.append(arr)
    for j in range(100):    # 세로
        num = 0
        for k in range(100):
            num += bingo[k][j]
        if num > max_num:
            max_num = num
    temp_num = 0
    for z in range(100):
        temp_num += bingo[z][z]
        if temp_num > max_num:
            max_num = temp_num
    temp_num = 0
    for z in range(100):
        temp_num += bingo[99-z][z]
        if temp_num > max_num:
            max_num = temp_num
    print(f"#{t}", max_num)