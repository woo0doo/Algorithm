k, n = map(int, input().split())
lanson = []
for i in range(k): lanson.append(int(input()))
start, end = 1, max(lanson)
answer = 0
while start <= end:
    mid = (start + end) // 2
    num = 0
    for len in lanson:
        num += len // mid
    if num >= n:
        start = mid + 1
    else: end = mid - 1
print(end)