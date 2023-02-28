n = int(input())
cnt=0
for i in range(n):
    res=[]
    word=input()
    res.append(word[0])
    for j in range(1,len(word)):
        res.append(word[j])
        if res[-1] == res[-2]:
            res.pop()
    setres=set(res)
    if len(setres) == len(res):
        cnt+=1
print(cnt)