import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))
stack = []
result = [-1] * N
for i in range(N-1,-1,-1):
    cnt = 0
    if not stack:
        stack.append((i, top[i]))
        continue
    for j in range(len(stack) -1, -1, -1):
        if stack[j][1] <= top[i]:
            result[stack[j][0]] = i
            stack.pop()
        else:
            stack.append((i, top[i]))
            break
    if not stack:
        stack.append((i, top[i]))

for r in result:
    print(r+1, end=' ')