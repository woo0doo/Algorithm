def solution(A, B):
    cnt = 0
    if (A == B):
        return cnt
    for i in range(len(A)):
        cnt += 1
        A = A[-1] + A[:len(A)-1]
        if (A == B):
            break
    return cnt if A == B else -1