import math

n,m=map(int,input().split())

result = int(math.factorial(n)) // int((math.factorial(n - m)) * math.factorial(m))
print(result)