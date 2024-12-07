import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

# 1부터 N까지 자연수를 M번 뽑아 나열 (중복 허용)
results = product(range(1, N + 1), repeat=M)

# 결과 출력
for result in results:
    print(' '.join(map(str, result)))
