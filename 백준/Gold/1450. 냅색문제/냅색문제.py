import sys
from bisect import bisect_right

def get_subsets(weights):
    subsets = []
    n = len(weights)
    for i in range(1 << n):  # 2^n개의 부분 집합
        total_weight = 0
        for j in range(n):
            if i & (1 << j):  # j번째 물건을 부분 집합에 포함
                total_weight += weights[j]
        subsets.append(total_weight)
    return subsets

def meet_in_the_middle(N, C, weights):
    # 1. 물건을 두 그룹으로 나눈다.
    first_half = weights[:N // 2]
    second_half = weights[N // 2:]

    # 2. 각 그룹의 부분 집합의 합을 구한다.
    subset1 = get_subsets(first_half)
    subset2 = get_subsets(second_half)

    # 3. 두 번째 그룹의 부분 집합의 합을 정렬
    subset2.sort()

    # 4. 첫 번째 그룹의 각 부분 집합에 대해 두 번째 그룹에서 가능한 최대 값을 찾는다.
    count = 0
    for weight1 in subset1:
        # 이분 탐색으로 weight1 + weight2 <= C를 만족하는 최대 weight2 찾기
        remaining_capacity = C - weight1
        count += bisect_right(subset2, remaining_capacity)

    return count

# 입력 처리
input = sys.stdin.read
data = input().strip().split('\n')
N, C = map(int, data[0].split())
weights = list(map(int, data[1].split()))

# 결과 계산 및 출력
print(meet_in_the_middle(N, C, weights))

