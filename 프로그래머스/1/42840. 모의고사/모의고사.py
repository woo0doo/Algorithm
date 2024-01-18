def solution(answers):
    student_a = [1,2,3,4,5]
    student_b = [2,1,2,3,2,4,2,5]
    student_c = [3,3,1,1,2,2,4,4,5,5]
    
    a = 0
    b = 0
    c = 0
    answer=[]
    for i in range(len(answers)):
        if student_a[i%5] == answers[i]:
            a+=1
        if student_b[i%8] == answers[i]:
            b+=1
        if student_c[i%10] == answers[i]:
            c+=1
    max_cnt = max(a,b,c)
    print(max_cnt)
    if a == max_cnt:
        answer.append(1)
    if b == max_cnt:
        answer.append(2)
    if c== max_cnt:
        answer.append(3)
    return answer