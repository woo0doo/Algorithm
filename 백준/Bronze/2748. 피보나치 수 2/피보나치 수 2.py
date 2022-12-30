n = int(input())

fib = [1,1]
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for i in range(3,n):
        temp = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = temp
    print(fib[0] + fib[1])