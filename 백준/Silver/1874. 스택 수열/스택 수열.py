n=int(input())
stack=[]
res=[]
cnt=1
noCnt=0
for i in range(n):
    num=int(input())

    while cnt <= num :
        stack.append(cnt)
        res.append("+")
        cnt+=1

    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        noCnt=1
        break

if noCnt == 0:
    print(*res, sep="\n")