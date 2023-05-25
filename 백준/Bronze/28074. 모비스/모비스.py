a=input()
arr=["M","O","B","I","S"]
for i in a:
    if i in arr:
        arr.pop(arr.index(i))

if arr:
    print("NO")
else:
    print("YES")