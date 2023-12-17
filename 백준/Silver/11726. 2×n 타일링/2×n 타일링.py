n = int(input())

d = [0 for _ in range(n)]

# n1 = 1, n2 = 2, n3 = 3, n4 = 5, n5 = 8 피보나치? 



for i in range(n):
    if i == 0:
        d[i] = 1
    elif i == 1:
        d[i] = 2
    else:
        d[i] = d[i - 2] + d[i - 1]

print(d[n-1]%10007) # 아 나머지 안나눴네