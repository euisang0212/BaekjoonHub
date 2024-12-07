import sys

# 입력 받기
data = sys.stdin.readline().strip()

# 각 문자를 내림차순으로 정렬
result = sorted(data, reverse=True)

# 결과 출력
print("".join(result))
