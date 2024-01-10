import itertools
from itertools import product

n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]

combi = list(itertools.product(numbers, repeat=m))
for i in range(len(combi)):
    for j in range(m):
        print(combi[i][j], end=' ')
    print()
