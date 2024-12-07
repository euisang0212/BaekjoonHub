import sys

result = []
N = int(sys.stdin.readline())  # N은 입력받은 정수

for _ in range(N):
    result.append(int(sys.stdin.readline()))  # 각 숫자를 리스트에 추가

result.sort()  # 리스트 정렬

print("\n".join(map(str, result)))  # 정렬된 결과를 출력
