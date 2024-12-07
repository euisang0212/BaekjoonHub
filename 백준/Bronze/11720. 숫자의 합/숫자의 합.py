import sys

result = 0
n = int(sys.stdin.readline().strip())
data = str(sys.stdin.readline().strip())


for i in range(n):
    result += int(data[i])
    
print(result)