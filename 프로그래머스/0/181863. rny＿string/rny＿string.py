def solution(rny_string):
    answer = ''
    answer = ''.join('rn' if ch == 'm' else ch for ch in rny_string)
    return answer