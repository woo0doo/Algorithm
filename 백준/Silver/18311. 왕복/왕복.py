import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    k -= arr[i]
    if k < 0:
        print(i+1)
        sys.exit()

for j in range(len(arr)):
    k -= arr[len(arr)-j-1]
    if k < 0:
        print(len(arr)-j)
        sys.exit()
