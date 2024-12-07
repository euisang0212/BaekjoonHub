import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

results = combinations(range(1, N+1), M)

for result in results:
    print(" ".join(map(str, result)))