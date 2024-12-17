import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

print(f"{nums[0]} {nums[N-1]}")