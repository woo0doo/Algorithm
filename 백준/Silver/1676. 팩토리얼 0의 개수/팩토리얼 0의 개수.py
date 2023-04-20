import math
n=int(input())

factorial = str(math.factorial(n))
cnt=0
for i in factorial[::-1]:
     if i == '0':
          cnt+=1
     else:
          break
print(cnt)