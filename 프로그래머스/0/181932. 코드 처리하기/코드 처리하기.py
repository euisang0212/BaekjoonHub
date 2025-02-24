def solution(code):
    answer = ''
    n = len(code)
    print(n)
    mode = 0
    
    for i in range(n):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
        else:
            if mode == 0:
                if i%2 == 0:
                    answer += code[i]
                else:
                    continue
            if mode == 1:
                if i%2 == 1:
                    answer += code[i]
                else:
                    continue
                
    if answer == '':
        answer = 'EMPTY'
    return answer