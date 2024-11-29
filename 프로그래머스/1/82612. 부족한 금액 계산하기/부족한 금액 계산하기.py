def solution(price, money, count):
    answer = -1
    total_price = 0
    
    for i in range(count):
        total_price += (price*(i+1))
    
    n = money - total_price
    if n >= 0:
        answer = 0
    else:
        answer = -n
    return answer