import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0

for hour in range(n+1):
    if hour < 10:
        hour = "0" + str(hour)
    hour = str(hour)
    for minute in range(60):
        if minute < 10:
            minute = "0" + str(minute)
        minute = str(minute)
        for second in range(60):
            if second < 10:
                second = "0" + str(second)
            second = str(second)
            if str(k) in (hour + minute + second):
                cnt += 1
print(cnt)