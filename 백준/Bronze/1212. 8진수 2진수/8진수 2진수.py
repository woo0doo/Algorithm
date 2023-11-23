n = int(input())

answer = '0o' + str(n)
print(bin(int(answer, 8))[2:])