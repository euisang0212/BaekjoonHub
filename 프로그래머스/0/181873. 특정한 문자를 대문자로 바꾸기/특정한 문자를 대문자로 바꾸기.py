def solution(my_string, alp):
    answer = ''
    answer = ''.join([ch.upper() if ch == alp else ch for ch in my_string])
#    answer = ''.join(upper(alp)) if _ == alp else ''.join(_) for _ in mystring
    return answer