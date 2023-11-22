def solution(babbling):
    result = 0
    for i in babbling:
        i = i.replace("aya", " ", 1)
        i = i.replace("ye", " ", 1)
        i = i.replace("woo", " ", 1)
        i = i.replace("ma", " ", 1)
        if i.isspace():
            result += 1
    return result