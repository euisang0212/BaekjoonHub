import sys
h, m = map(int, sys.stdin.readline().strip().split())
C = int(sys.stdin.readline())

t = h*60 + m + C

if t >= 24*60:
    t = t - (24*60)

print(f"{t//60} {t%60}")