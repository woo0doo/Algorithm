import heapq
import sys
input=sys.stdin.readline
n=int(input())
card=list(int(input()) for _ in range(n))
heapq.heapify(card)
answer=0

while len(card) != 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    sum = first + second
    answer += sum
    heapq.heappush(card, sum)

print(answer)