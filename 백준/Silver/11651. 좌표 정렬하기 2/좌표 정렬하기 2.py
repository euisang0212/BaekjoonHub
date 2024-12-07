import sys

N = int(sys.stdin.readline().strip())
data = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    data.append((x, y))

data.sort(key=lambda x: (x[1], x[0]))

for x,y in data:
    print(x, y)