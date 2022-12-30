a=[]
for i in range(5):
    a.append(int(input()))

avg=int(sum(a)/5)
print(avg)
a.sort()
print(a[2])
