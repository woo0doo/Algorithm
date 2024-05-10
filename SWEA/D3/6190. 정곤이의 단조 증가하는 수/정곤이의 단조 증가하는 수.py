T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = -1

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = nums[i] * nums[j]
            str_num = str(result)
            flag = True
            for k in range(len(str_num)):
                if len(str_num) == 1:
                    break
                if k == len(str_num) -1:
                    break
                if int(str_num[k]) > int(str_num[k+1]):
                    flag = False
            if flag == True:
                max_num = max(max_num, result)
    print(f'#{t}', max_num)