import sys

N = int(sys.stdin.readline().strip())

for i in range(9):
    print(f"{N} * {i+1} = {N*(i+1)}")