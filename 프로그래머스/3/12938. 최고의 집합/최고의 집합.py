def solution(n, s):
    answer = []
    
    if s < n:
        return [-1] # 그냥 -1 안됨, [-1]
    
    q, r = divmod(s, n)
    
    answer = [q] * n
    print(answer)
    
    for i in range(r):
        answer[i] += 1
    print(answer)
        
    return sorted(answer)