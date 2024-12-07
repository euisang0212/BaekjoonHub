import sys
data = []
N = int(sys.stdin.readline().strip())

for i in range(N):
    data.append(int(sys.stdin.readline()))
    
data.sort()

print("\n".join(map(str, data)))