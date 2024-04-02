word = input()

string_word = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        string_word.add(word[i:j+1])

print(len(string_word))
