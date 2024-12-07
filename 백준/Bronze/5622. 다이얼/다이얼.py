import sys

s = sys.stdin.readline().strip()

result = 0

for i in range(len(s)):
    if s[i] in ['A', 'B', 'C']:
        result += 3
    elif s[i] in ['D', 'E', 'F']:
        result += 4
    elif s[i] in ['G', 'H', 'I']:
        result += 5
    elif s[i] in ['J', 'K', 'L']:
        result += 6
    elif s[i] in ['M', 'N', 'O']:
        result += 7
    elif s[i] in ['P', 'Q', 'R', 'S']:
        result += 8
    elif s[i] in ['T', 'U', 'V']:
        result += 9
    elif s[i] in ['W', 'X', 'Y', 'Z']:
        result += 10
    else:
        result += 11

print(result)