import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
k = int(input())

card = []
result = set()
for _ in range(n):
    card.append(input().rstrip())

per = list(permutations(card, k))
for i in range(len(per)):
    word = ''
    for j in range(len(per[i])):
        word += per[i][j]
    result.add(word)

result = list(result)
print(len(result))