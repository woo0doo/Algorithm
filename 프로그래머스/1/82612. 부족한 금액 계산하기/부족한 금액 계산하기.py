def solution(price, money, count):
    cnt = count*(count+1)/2
    total_price = price * cnt
    result = total_price - money
    if result > 0:
        return result
    else:
        return 0