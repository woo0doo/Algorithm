board=list(map(str,input().split('.')))
result=[]
flag=True

for i in board:
    if len(i)%2==1:
        flag=False

    result.append((len(i)//4)*"AAAA")
    result.append((len(i)%4)*"B")
    result.append('.')

if flag==False:
    print(-1)
else:
    result.pop()
    for i in result:
        print(i,end='')
