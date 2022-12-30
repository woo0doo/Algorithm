arr = []
for i in range(10):
    n = int(input())
    if (n%42 in arr) == False:
        arr.append(n%42)
print(len(arr))