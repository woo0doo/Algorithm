from collections import deque

def solution(progresses, speeds):
    deq = deque(progresses)
    deq_speeds = deque(speeds)
    answer = []
    while deq:
        for i in range(len(deq_speeds)):
            deq[i] += deq_speeds[i]
        cnt = 0
        while deq and deq[0] >= 100:
            cnt+=1
            deq.popleft()
            deq_speeds.popleft()
        if (cnt > 0):
            answer.append(cnt)
    return answer