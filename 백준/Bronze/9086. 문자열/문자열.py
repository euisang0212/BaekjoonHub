import sys

n = int(sys.stdin.readline())
for i in range(n):
    result = ""
    s = str(sys.stdin.readline().strip())
    result += s[0]
    result += s[-1]
    print(result)