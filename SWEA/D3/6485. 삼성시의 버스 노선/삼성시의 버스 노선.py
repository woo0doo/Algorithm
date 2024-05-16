T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [0] * 5_001
    for n in range(N):
        a,b = map(int, input().split())
        for i in range(b-a+1):
            arr[a+i] += 1

    P = int(input())
    result = []
    for p in range(P):
        C = int(input())
        result.append(arr[C])

    print(f'#{t} ', end='')
    for i in result:
        print(i, end=' ')
    print()
