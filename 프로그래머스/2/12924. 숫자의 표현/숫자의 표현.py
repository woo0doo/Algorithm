def solution(n):
    answer = 0
    for start_num in range(1,n+1):
        sum_number = 0
        num = start_num
        while True:
            sum_number += num
            if sum_number > n:
                break
            elif sum_number == n:
                answer += 1
                break
            else:
                num+=1
    return answer