from itertools import combinations

n, m = map(int, input().split())

numbers = [i for i in range(1,n+1)]

combi = list(combinations(numbers, m))
for i in range(len(combi)):
    for j in range(m):
        print(combi[i][j], end=' ')
    print()