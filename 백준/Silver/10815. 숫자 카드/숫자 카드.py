import sys
sys.stdin.readline()
A = set(sys.stdin.readline().split())
sys.stdin.readline()
B = list(sys.stdin.readline().split())
for c in B:
    print(1, end=' ') if c in A else print(0, end=' ')