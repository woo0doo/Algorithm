T = 10

for _ in range(T):
    t = int(input())
    find_string = input()
    word = input()

    word_split = word.split(find_string)
    print(f'#{t}', len(word_split)-1)
