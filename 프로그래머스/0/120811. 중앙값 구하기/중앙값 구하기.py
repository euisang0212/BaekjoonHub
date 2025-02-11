def solution(array):
    answer = 0
    n = len(array)

    array.sort()

    a = int((n+1)/2)
    answer = array[a-1]
    return answer