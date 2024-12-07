import sys
import string

s = sys.stdin.readline().strip()

alphabet_dict = {char: -1 for char in string.ascii_lowercase}

for i in range(len(s)):
    if s[i] in alphabet_dict:
        if alphabet_dict[s[i]] == -1:
            alphabet_dict[s[i]] = i
            
# 딕셔너리 value만 공백으로 구분하여 출력
print(" ".join(map(str, alphabet_dict.values())))