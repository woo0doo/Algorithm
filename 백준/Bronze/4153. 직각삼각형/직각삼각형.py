while True:
    n=list(map(int,input().split()))
    if (n[0] or n[1] or n[2]) == 0:
        break
    n.sort(reverse=True)
    if n[0]*n[0] == n[1]*n[1] + n[2]*n[2]:
        print("right")
    else:
        print("wrong")