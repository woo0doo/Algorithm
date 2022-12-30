arr = []
for i in range(9):
    x = int(input())
    arr.append(x)
print(max(arr))
for i in range(9):
    if arr[i] == max(arr):
        print(i+1)
