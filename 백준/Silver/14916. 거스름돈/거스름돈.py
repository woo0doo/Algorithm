import sys

n = int(input())

cnt = 0

if n % 10 == 1:
    cnt += 3
    n -= 6

elif n % 10 == 3:
    cnt += 4
    n -= 8

elif n % 10 == 6:
    cnt += 3
    n -= 6

elif n % 10 == 8:
    cnt += 4
    n -= 8
else:
    cnt += n//5
    n %= 5
    cnt += n//2
    n %= 2

if (n < 0):
    print(-1)
    sys.exit()
cnt += n//5
n %= 5
print(cnt)