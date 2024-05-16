T = int(input())

for t in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    a_group = []
    b_group = []
    if N%2 == 0:
        a_group = cards[0:N // 2]
        b_group = cards[N // 2:]
    else:
        a_group = cards[0:N//2+1]
        b_group = cards[N//2+1:]

    result = []
    for i in range(len(b_group)):
        result.append(a_group[i])
        result.append(b_group[i])
    if N % 2 == 1:
        result.append(a_group[-1])

    print(f'#{t} ', end='')
    for card in result:
        print(card, end=' ')
    print()