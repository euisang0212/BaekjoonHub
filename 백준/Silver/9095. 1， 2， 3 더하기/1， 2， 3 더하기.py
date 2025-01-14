import sys

def cal(n):
    # 최대 n은 11
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp


data = sys.stdin.read().split()
T = int(data[0])  # 테스트 케이스 개수(첫째줄 제외 입력 라인 수)
test_cases = list(map(int, data[1:]))

max_n = max(test_cases)
dp = cal(max_n)

for n in test_cases:
    print(dp[n])