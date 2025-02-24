def solution(num_list):
    answer = 0
    first = 1
    for i in range(len(num_list)):
        first *= num_list[i]
    
    b = sum(num_list)
    
    if first < (b**2):
        answer = 1
    else:
        answer = 0
    
    return answer