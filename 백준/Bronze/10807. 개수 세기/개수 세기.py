import sys

counts = 0
N = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

x = int(sys.stdin.readline().strip())

for i in range(N):
    if nums[i] == x:
        counts += 1
        
print(counts)