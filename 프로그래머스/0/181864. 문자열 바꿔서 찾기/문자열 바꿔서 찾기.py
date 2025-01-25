def solution(myString, pat):
    answer = 0
    check = ''.join('A' if ch == 'B' else 'B' for ch in myString)
    print(check)
    if pat in check:
        answer = 1
    else:
        answer = 0
    return answer