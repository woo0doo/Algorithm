a,b=input().split()
num_a=''
num_b=''
for i in range(1,len(a)+1):
    num_a+=a[-i]
for j in range(1,len(b)+1):
    num_b+=b[-j]
if int(num_a) >= int(num_b):
    print(int(num_a))
else:
    print(int(num_b))
    