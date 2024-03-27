import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
result = 0
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

while True:
    if len(heap) == 1:
        break
    minNum = heapq.heappop(heap)
    minNum2 = heapq.heappop(heap)
    addNumber = minNum + minNum2
    result += addNumber
    heapq.heappush(heap, addNumber)

print(result)
