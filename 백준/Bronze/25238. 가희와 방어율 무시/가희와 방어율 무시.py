mon,human = map(int, input().split())
human *= 0.01
if mon - (mon*human) >= 100:
    print(0)
else:
    print(1)
