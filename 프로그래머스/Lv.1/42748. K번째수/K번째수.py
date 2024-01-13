def solution(array, commands):
    result = []
    for i in commands:
        sort_i = sorted(array[(i[0]-1):i[1]])
        result.append(sort_i[i[2]-1])
    return result