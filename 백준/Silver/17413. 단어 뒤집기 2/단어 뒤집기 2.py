import sys
input=sys.stdin.readline

arr=list(map(str,input().rstrip()))

stack=[]
rev=[]
for i in arr:
    if i == '<':
        if rev:
            for j in rev[::-1]:
                print(j,end='')
            rev=[]
        stack.append('<')
        print('<',end='')
    elif i == '>':
        stack.pop()
        print('>',end='')
    elif i == ' ':
        if stack:
            print(i,end='')
        else:
            for j in rev[::-1]:
                print(j,end='')
            print(' ',end='')
            rev=[]
    else:
        if stack:
            print(i,end='')
        else:
           rev.append(i)


if rev:
    for j in rev[::-1]:
        print(j,end='')