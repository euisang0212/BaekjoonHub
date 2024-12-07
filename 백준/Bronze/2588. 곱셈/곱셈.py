import sys

#a, b = map(int, sys.stdin.readline().split())
a = int(sys.stdin.readline().strip())
b = str(sys.stdin.readline().strip())

print(a*int(b[-1]))
print(a*int(b[-2]))
print(a*int(b[-3]))
print(a*int(b))