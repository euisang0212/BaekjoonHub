import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    A, B = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")