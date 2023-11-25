word = input()

quack = []
cnt = 0
result = False

for i in word:
    result = False
    if i == "q":
        quack.append(["q"])
        result = True
        cnt = max(len(quack), cnt)

    elif i == "u":
        for j in range(len(quack)):
            if quack[j] == ["q"]:
                quack[j] = ["qu"]
                result = True
                break

        cnt = max(len(quack), cnt)
    elif i == "a":
        for j in range(len(quack)):
            if quack[j] == ["qu"]:
                quack[j] = ["qua"]
                result = True
                break

        cnt = max(len(quack), cnt)

    elif i == "c":
        for j in range(len(quack)):
            if quack[j] == ["qua"]:
                quack[j] = ["quac"]
                result = True
                break

            cnt = max(len(quack), cnt)

    elif i == "k":
        for j in range(len(quack)):
            if quack[j] == ["quac"]:
                quack.remove(quack[j])
                result = True
                break
        cnt = max(len(quack), cnt)
    if not result:
        break

if result == False or len(quack) > 0:
    print(-1)
else:
    print(cnt)
