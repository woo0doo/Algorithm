import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word_list = []
for i in range(n):
    word_list.append(input().rstrip())

answer = ""
hap = 0
for i in range(m):
    a, t, g, c = 0, 0, 0, 0
    for j in range(n):
        if word_list[j][i] == "A":
            a += 1
        elif word_list[j][i] == "T":
            t += 1
        elif word_list[j][i] == "G":
            g += 1
        elif word_list[j][i] == "C":
            c += 1

    if max(a, c, g, t) == a:
        answer += 'A'
        hap += c + g + t
    elif max(a, c, g, t) == c:
        answer += 'C'
        hap += a + g + t
    elif max(a, c, g, t) == g:
        answer += 'G'
        hap += a + c + t
    elif max(a, c, g, t) == t:
        answer += 'T'
        hap += c + g + a

print(answer)
print(hap)
