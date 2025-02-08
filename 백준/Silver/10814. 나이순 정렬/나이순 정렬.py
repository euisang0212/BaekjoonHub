import sys
data = sys.stdin.read().strip().split("\n")
N = int(data[0])
members = []

for i in range(N):
    age, name = data[i+1].split()
    members.append((int(age), name))
        
members.sort(key=lambda member: member[0])
        
for age, name in members:
    print(age, name)