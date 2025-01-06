def solution(numbers):
    answer = ''
    
    number = list(map(str, numbers))
#    print(number)

    number.sort(key = lambda x : x*3, reverse=True)
#    print(number)

    for i in number:
        answer += i
    
    
    
    return str(int(answer))     # 00, 000 이런 케이스