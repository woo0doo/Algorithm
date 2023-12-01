import sys
a, b = map(int, input().split())
cnt = 1
while (b != a):
    if b == 1 or str(b)[-1] in ["3", "5", "7", "9"]:
        print(-1)
        sys.exit()

    if b != 1 and b % 10 == 1:
        b = b//10
        cnt += 1
    else:
        b = b // 2
        cnt += 1

print(cnt)