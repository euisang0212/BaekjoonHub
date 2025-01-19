def solution(arr):
    n = len(arr) // 2 + 1  # 숫자의 개수
    max_dp = [[float('-inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]

    # 초기화: 숫자만 있는 경우
    for i in range(n):
        max_dp[i][i] = int(arr[2 * i])
        min_dp[i][i] = int(arr[2 * i])

    # 구간 길이 2부터 n까지
    for length in range(1, n):  # length: 구간의 길이
        for i in range(n - length):  # 시작점
            j = i + length  # 끝점
            for k in range(i, j):  # 중간 분할점
                op = arr[2 * k + 1]  # 연산자
                if op == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                elif op == '-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])

    return max_dp[0][n - 1]
