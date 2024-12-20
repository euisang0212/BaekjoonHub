import sys

num = []

for i in range(9):
    num.append(int(sys.stdin.readline().strip()))

max_num = max(num)
max_index = num.index(max_num) + 1
    
print(max_num)
print(max_index)