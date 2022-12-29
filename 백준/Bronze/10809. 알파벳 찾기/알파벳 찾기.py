import sys
n=sys.stdin.readline()
for i in range(26):
    print(n.find(chr(ord('a')+i)), end=' ')
    
