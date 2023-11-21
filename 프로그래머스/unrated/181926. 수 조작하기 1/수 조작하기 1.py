def solution(n, control):
    for i in range(len(control)):
        idx_str = control[i]
        if idx_str == "w":
            n += 1
        elif idx_str == "s":
            n -= 1
        elif idx_str == "d":
            n += 10
        else:
            n -= 10
    return n