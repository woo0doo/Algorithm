n=int(input())

num=str(665)
res = 0
while res!=n:
    num = str(int(num)+1)
    if "666" in num:
        res += 1
    
print(num)
