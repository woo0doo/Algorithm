while True:
    n=input()
    fail=0
    if n == "0":
        break
    word=[]
    for i in range(1,len(n)+1):
        word.append(n[-i])

    for i in range(len(n)):
        if word[i] != n[i]:
            print("no")
            fail=1
            break
    if fail == 0:
        print("yes")
