from itertools import combinations

def solution(nums):
    set_nums = set(nums)
    return min(len(set_nums), len(nums)//2)
        