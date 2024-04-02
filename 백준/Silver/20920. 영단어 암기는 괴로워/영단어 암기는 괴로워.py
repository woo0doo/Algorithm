import sys
input = sys.stdin.readline
N,M = map(int, input().split())

dictionary = dict()

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

result = sorted(dictionary.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in result:
    print(i[0])
