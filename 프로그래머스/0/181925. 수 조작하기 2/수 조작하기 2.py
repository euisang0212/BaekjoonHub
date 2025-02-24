def solution(numLog):
    answer = ''
    
    n = len(numLog)
    
    a = numLog[0]
    
    for i in range(1, n):
        a = numLog[i] - numLog[i-1]
        if a == 1:
            answer += 'w'
        elif a == -1:
            answer += 's'
        elif a == 10:
            answer += 'd'
        elif a == -10:
            answer += 'a'
    return answer