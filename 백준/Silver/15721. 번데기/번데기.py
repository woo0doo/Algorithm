import sys
input = sys.stdin.readline

people = int(input())
t = int(input())
sign = int(input())
bbun_cnt = 0
daegi_cnt = 0
game_cnt = 2
while True:
    for _ in range(2):
        bbun_cnt += 1
        if sign == 0:
            if bbun_cnt == t:
                print((bbun_cnt + daegi_cnt - 1) % people)
                sys.exit()
        daegi_cnt += 1
        if sign == 1:
            if daegi_cnt == t:
                print((bbun_cnt + daegi_cnt - 1) % people)
                sys.exit()
    for i in range(game_cnt):
        bbun_cnt += 1
        if sign == 0:
            if bbun_cnt == t:
                print((bbun_cnt + daegi_cnt-1) % people)
                sys.exit()

    for j in range(game_cnt):
        daegi_cnt += 1
        if sign == 1:
            if daegi_cnt == t:
                print((bbun_cnt + daegi_cnt-1) % people)
                sys.exit()
    game_cnt += 1