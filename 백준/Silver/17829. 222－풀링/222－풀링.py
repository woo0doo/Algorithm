n=int(input())
nums=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    nums.append(tmp)
def pooling(size, x, y):
    if size == 2:
        arr = [nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        arr.sort()
        return arr[-2]
    mid = size // 2
    lt = pooling(mid, x, y)
    rt = pooling(mid, x + mid, y)
    lb = pooling(mid, x, y + mid)
    rb = pooling(mid, x + mid, y + mid)
    answer=[lt, rt, lb, rb]
    answer.sort()
    return answer[-2]
print(pooling(n, 0, 0))