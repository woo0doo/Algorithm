import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(list(map(int, input().split())))
stack = []
target_number = 1

while True:
    if len(arr) == 0 and len(stack) == 0:
        break
    if len(arr) == 0 and stack[-1] != target_number:
        print("Sad")
        sys.exit()


    if stack and stack[-1] == target_number:
        stack.pop()
        target_number+=1
    elif arr[0] == target_number:
        arr.popleft()
        target_number += 1
    else:
        stack.append(arr.popleft())

print("Nice")