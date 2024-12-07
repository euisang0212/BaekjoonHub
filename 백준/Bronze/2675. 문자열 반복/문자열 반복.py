import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    result = ""
    R, S = sys.stdin.readline().strip().split()
    R = int(R)
    
    for j in range(len(S)):
        result += S[j] * R

    print(result)