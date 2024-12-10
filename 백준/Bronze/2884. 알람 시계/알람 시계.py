import sys

h, m = map(int, sys.stdin.readline().strip().split())

original_min = h*60 + m

new_min = original_min - 45

if new_min < 0:
    result = (24*60) + new_min
else:
    result = new_min
    
print(f"{result//60} {result%60}")