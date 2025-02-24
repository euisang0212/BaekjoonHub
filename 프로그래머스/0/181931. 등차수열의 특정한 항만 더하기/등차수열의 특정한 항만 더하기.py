def solution(a, d, included):
    answer = 0
    array = [a]
    n = len(included)
    
    for i in range(n-1):
        array.append(array[i]+d)

    for i in range(n):
        if included[i]:
            answer += array[i]
    
    
    print(array)
        
    return answer