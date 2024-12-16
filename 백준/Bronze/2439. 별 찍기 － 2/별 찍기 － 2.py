import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    str = " "*(N-i-1) + "*"*(i+1)
    print(str)