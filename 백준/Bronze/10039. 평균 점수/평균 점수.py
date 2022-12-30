n=[]
for i in range(5):
    n1=int(input())
    if n1 < 40:
        n1=40
    n.append(n1)

avg=sum(n)/5

print(int(avg))