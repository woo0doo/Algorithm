N, M = map(int,input().split())

arr = []
def backTracking():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N+1):
        arr.append(i)
        backTracking()
        arr.pop()

backTracking()