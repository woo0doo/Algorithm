
def backtracking(S, B, idx, cnt):
    global answer
    if cnt != 0:
        if abs(S - B) < answer:
            answer = abs(S - B)
    if idx >= N:
        return
    backtracking(S * foods[idx][0], B + foods[idx][1], idx+1, cnt+1)
    backtracking(S, B, idx+1, cnt)

N = int(input())
answer = float('inf')
foods = [list(map(int, input().split())) for i in range(N)]
backtracking(1, 0, 0, 0)
print(answer)