import sys

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    A, B = map(int, line.split())
    print(A+B)
    