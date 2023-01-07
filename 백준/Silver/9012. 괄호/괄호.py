import sys

n=int(input())


for _ in range(n):
    result=sys.stdin.readline().rstrip()
    stack=[]
    break_point=False
    for i in result:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break_point=True
                break
    if break_point == True:
        continue
    elif len(stack) != 0:
        print("NO")
    else:
        print("YES")                
