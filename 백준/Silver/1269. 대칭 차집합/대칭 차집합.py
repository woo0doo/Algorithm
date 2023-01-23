import sys

n,q=map(int,input().split())
m = set(map(int,sys.stdin.readline().split()))
t = set(map(int,sys.stdin.readline().split()))

res=len((m-t)) + len((t-m))
print(res)