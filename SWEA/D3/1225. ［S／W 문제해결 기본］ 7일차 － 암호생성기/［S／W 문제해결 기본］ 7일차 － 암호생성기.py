from collections import deque

T = 10

for _ in range(1, T+1):
    t = int(input())
    nums = deque(map(int, input().split()))
    cnt = 0
    while (nums[-1] > 0):
        popleft = nums.popleft()
        nums.append(popleft - (cnt % 5 +1))
        cnt += 1
    print(f'#{t}', end=' ')
    for num in nums:
        if num < 0:
            print(0, end=' ')
        else:
            print(num, end=' ')
    print()
