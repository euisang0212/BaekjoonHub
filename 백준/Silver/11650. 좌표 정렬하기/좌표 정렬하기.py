import sys

N = int(sys.stdin.readline().strip())
data = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x,y))
    
data.sort()

for x,y in data:
    print(x, y)