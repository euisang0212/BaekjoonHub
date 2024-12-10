import sys

n = int(sys.stdin.readline().strip())
result = 0

if n % 4 == 0:
    result = 1

if n % 100 == 0:
    result = 0

if n % 400 == 0:
    result = 1

print(result)