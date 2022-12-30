n = int(input())
result=0

def fibonacci(N):
    if N==0:
        result=0
        return result
    elif N==1:
        result = 1
        return result
    else:
        result = fibonacci(N-1)+fibonacci(N-2)
        return result

print(fibonacci(n))
