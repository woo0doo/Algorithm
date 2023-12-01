import sys
input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))
arr.sort()
if len(arr) % 2 == 1:
    max_strength = arr[-1]
    for i in range(len(arr)//2):
        strength = arr[i] + arr[len(arr)-2-i]
        max_strength = max(max_strength, strength)
    print(max_strength)
else:
    max_strength = 0
    for i in range(len(arr)//2):
        strength = arr[i] + arr[len(arr)-1-i]
        max_strength = max(max_strength, strength)
    print(max_strength)