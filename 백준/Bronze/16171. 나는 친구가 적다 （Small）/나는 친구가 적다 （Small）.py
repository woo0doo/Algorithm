arr1=input()
arr2=input()

result=""

for i in arr1:
    if i.isdigit():
        pass
    else:
        result+=i
if arr2 in result:
    print(1)
else:
    print(0)