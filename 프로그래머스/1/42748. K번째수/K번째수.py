def solution(array, commands):
    answer = []
    
    for cmd in commands:
        start, end, num = cmd
        new_arr = array[start-1:end]
        new_arr = sorted(new_arr)
        
        answer.append(new_arr[num-1])
    return answer