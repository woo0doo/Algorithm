import heapq
import sys

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_num = heapq.heappop(scoville)
        if min_num >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        else:
            second_min_num = heapq.heappop(scoville)
            heapq.heappush(scoville, second_min_num*2 + min_num)
            answer += 1
    return answer