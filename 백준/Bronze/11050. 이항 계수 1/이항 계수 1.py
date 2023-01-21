a,b=map(int,input().split())

result=1
div=1
for i in range(b):
    result *= a-i
for j in range(b):
    div *= j+1

print(int(result/div))