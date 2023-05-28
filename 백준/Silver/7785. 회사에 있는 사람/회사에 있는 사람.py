import sys
input=sys.stdin.readline
n=int(input())
room=set()
for i in range(n):
    a,b=map(str,input().rstrip().split())
    if b=="enter":
        room.add(a)
    else:
        room.remove(a)

list_room=list(room)
list_room.sort(reverse=True)
for i in list_room:
    print(i)


