num = int(input())

li=list(map(int,str(num)))
li.sort(reverse=True)

for i in li:
    print(i, end='')