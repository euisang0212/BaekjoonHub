import sys
x = ""
a, b = map(str, sys.stdin.readline().strip().split())

a = a[::-1]
b = b[::-1]

a = int(a)
b = int(b)

if a > b:
    print(a)
else:
    print(b)