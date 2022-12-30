n = int(input())
chong=["ChongChong"]
plus=1
result=0 
for i in range(n):
    a,b=input().split()                          ## a,b값 받음
    for j in range(0,plus):                     ## a==chong[j]인지 반복
        result=0
        if a==chong[j]:                         ## 반약 a==chong[j]이면 
            for k in range(0,plus):             ## b==chong[j]인지 돌림
                if b==chong[k]:                  ## b==chong[j]이면 result=1
                    result+=1
                    break
            if result == 1:                     ## result가 1이면 continue
                continue
            elif result == 0:                   ## 0이면 추가
                chong.append(b)             
                plus+=1
        elif b==chong[j]:                         ## 반약 a==chong[j]이면 
            for p in range(0,plus):             ## b==chong[j]인지 돌림
                if a==chong[p]:                  ## b==chong[j]이면 result=1
                    result+=1
                    break
            if result == 1:                     ## result가 1이면 continue
                continue
            elif result == 0:                   ## result 0이면 추가
                chong.append(a)             
                plus+=1
        else:
            continue
if len(chong) == 1:
    chong = []
print(len(chong))

