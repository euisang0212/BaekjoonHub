import sys

X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
total = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    total += a*b
    
if total == X:
    print("Yes")
else:
    print("No")