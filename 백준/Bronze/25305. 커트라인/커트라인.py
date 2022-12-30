import sys
a,b=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
num.sort()
print(num[-b])
