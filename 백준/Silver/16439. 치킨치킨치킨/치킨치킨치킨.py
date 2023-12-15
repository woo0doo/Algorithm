import sys
from itertools import permutations

# 치킨 3개를 입력받는데 최댓값을 출력해야함.
# 모든 경우의 수의 합 비교 ??
# 3개 정해서 그 중에서 제일 큰 값을 선택함.

input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
order = [i for i in range(m)]

for i in range(n):
    arr.append(list(map(int,input().split())))

per = list(permutations(order, 3))

maximum = 0
for i in range(len(per)):   # 순열 순서
    max_number = 0
    person = [0 for _ in range(n)]
    for j in range(3):  # 치킨 3개 다돌림
        for k in range(n):  # 그중 최댓값 저장
            person[k] = max(person[k], arr[k][per[i][j]])
    maximum = max(maximum, sum(person))

print(maximum)
