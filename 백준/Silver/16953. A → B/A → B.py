import sys

def min_operations(A, B):
    count = 1

    while B > A:
        if B % 2 == 0:  # B가 짝수인 경우
            B //= 2
        elif B % 10 == 1:  # 끝자리가 1인 경우
            B //= 10
        else:  # 만들 수 없는 경우
            return -1
        count += 1

    # B가 A와 같아지면 성공, 그렇지 않으면 실패
    return count if B == A else -1

A, B = map(int, sys.stdin.readline().split())
print(min_operations(A, B))
