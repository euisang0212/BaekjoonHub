import sys
data = []

for i in range(5):
    data.append(int(sys.stdin.readline().strip()))
    
data.sort()

print(sum(data)//5)
print(data[2])