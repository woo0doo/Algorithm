R = int(input())
a_s = 100
b_s = 100
for i in range(R):
    a,b = map(int,input().split())
    if a > b:
        b_s = b_s - a
    elif a < b:
        a_s = a_s - b
    else:
        continue
print(a_s)
print(b_s)