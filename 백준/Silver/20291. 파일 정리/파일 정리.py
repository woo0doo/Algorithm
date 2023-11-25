import sys
input = sys.stdin.readline

n = int(input())
file = dict()

for i in range(n):
    title, extension = input().rstrip().split(".")
    if not extension in file:
        file[extension] = 1
    else:
        file[extension] += 1

sort_file = sorted(file.items())
for key, value in sort_file:
    print(key, value)
