import sys

N = int(sys.stdin.readline().strip())

result = ""

for i in range(N//4):
    result += "long "

result += "int"

print(result)