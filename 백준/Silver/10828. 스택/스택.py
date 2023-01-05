import sys
n = int(input())
res=[]
for _ in range(n):
    ans=list(sys.stdin.readline().split())
    if ans[0] == 'push':
        res.append(ans[1])
    elif ans[0] == 'pop':
        if res:
            print(res.pop())
        else:
            print(-1)
    elif ans[0] == 'size':
        print(len(res))
    elif ans[0] == 'empty':
        if res:
            print(0)
        else:
            print(1)
    elif ans[0] == 'top':
        if res:
            print(res[-1])
        else:
            print(-1)