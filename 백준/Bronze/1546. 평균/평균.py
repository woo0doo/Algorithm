n = int(input())
result = 0
arr = list(map(int,input().split()))
for i in range(n):
    result += (arr[i] / max(arr)) * 100
print(result/n)
