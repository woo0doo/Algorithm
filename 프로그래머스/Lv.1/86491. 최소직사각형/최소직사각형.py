def solution(sizes):
    max_size = 0
    min_size = 0
    for i,j in sizes:
        max_cm = max(i,j)
        max_size = max(max_size, max_cm)
        min_cm = min(i,j)
        min_size = max(min_size, min_cm)
    return max_size * min_size