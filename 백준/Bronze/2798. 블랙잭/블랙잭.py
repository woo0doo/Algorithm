from itertools import combinations
import sys

input=sys.stdin.readline

n,m=map(int,input().split())

arr=list(map(int,input().split()))
big_sum=0
for i in combinations(arr,3):
    temp_sum=sum(i)
    if big_sum<temp_sum<=m:
        big_sum=temp_sum
print(big_sum)
