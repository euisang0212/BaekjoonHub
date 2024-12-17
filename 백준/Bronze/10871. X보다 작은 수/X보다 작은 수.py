import sys

result = []
N, X = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N):
    if nums[i] < X:
        result.append(f"{nums[i]}")
        
print(" ".join(result))