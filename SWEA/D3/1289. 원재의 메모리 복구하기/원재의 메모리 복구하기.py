T = int(input())

for _ in range(T):
    cnt = 0
    target = 0

    num_arr = list(map(int, input()))
    for num in num_arr:
        if num == target:
            continue
        else:
            target = num
            cnt+=1

    print(f'#{_+1}',cnt)
