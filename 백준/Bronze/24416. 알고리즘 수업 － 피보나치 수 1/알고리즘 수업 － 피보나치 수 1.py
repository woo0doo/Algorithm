def fibo1(n):
    global count1
    if (n == 1) or (n == 2):
        count1 += 1
        return 1
    else:
        return fibo1(n - 1) + fibo1(n - 2)


f = [0] * 50


def fibo2(n):
    global count2
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count2 += 1
    return f[n]
count1 = 0
count2 = 0

n = int(input())

fibo1(n)
fibo2(n)
print(count1, count2)
