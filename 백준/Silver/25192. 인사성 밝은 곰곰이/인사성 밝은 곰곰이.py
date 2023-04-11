import sys
input=sys.stdin.readline
n=int(input())
cnt=0
chat=set()

for i in range(n):
    a=input().rstrip()
    if a == "ENTER":
        chat.clear()
    else:
        if a in chat:
            pass
        else:
            chat.add(a)
            cnt+=1
print(cnt)