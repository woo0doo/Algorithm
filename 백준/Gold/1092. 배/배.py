import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))

M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
if crane[0] < box[0]:
    print(-1)
    exit()
cnt = 0
while box:
    cnt += 1
    for i in crane:
        for j in box:
            if i >= j:
                box.remove(j)
                break

print(cnt)