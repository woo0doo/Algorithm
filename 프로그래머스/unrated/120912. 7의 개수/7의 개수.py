def solution(array):
    cnt = 0
    for i in array:
        i = str(i)
        for j in i:
            if j == '7':
                cnt += 1
    return cnt
