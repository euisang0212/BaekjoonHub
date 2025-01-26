"""from math import sqrt

def solution(r1, r2):
    count = 0

    for x in range(0, r2 + 1):  # x 값 순회
        max_y = int(sqrt(r2**2 - x**2))  # 바깥 원의 최대 y 값
        min_y = int(sqrt(r1**2 - x**2)) + 1 if x < r1 else 0  # 안쪽 원의 최소 y 값

        # x > 0일 때 y = 0 제외
        count += max_y - min_y + 1

    # 전체 점 개수는 4배 (대칭성) 적용
    total_count = count * 4

    # x축과 y축에서 중복되는 점 제외
    total_count -= (r2 - r1 + 1) * 4

    return total_count

"""


from math import ceil, floor, sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        if i < r1:
            answer += (floor(sqrt(r2*r2-i*i)) - ceil(sqrt(r1*r1-i*i))+1)
        else:
            answer += (floor(sqrt(r2*r2-i*i))+1)
    answer *=4
    return answer
