def solution(n):
    word = str(n)
    result=[]
    for i in word[::-1]:
        result.append(int(i))
    return result