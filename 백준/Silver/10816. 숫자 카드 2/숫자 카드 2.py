import sys
input=sys.stdin.readline

n=int(input())

N=list(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))

hashmap = {}

for i in N:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
print(' '.join(str(hashmap[k]) if k in hashmap else '0' for k in M))