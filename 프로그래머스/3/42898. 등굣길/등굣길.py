def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점

    # 웅덩이를 -1로 표시
    for x, y in puddles:
        dp[y][x] = -1

    # DP로 최단 경로 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 웅덩이는 0으로 처리
                dp[i][j] = 0
                continue
            if i > 1:
                dp[i][j] += dp[i - 1][j]  # 위쪽에서 오는 경우
            if j > 1:
                dp[i][j] += dp[i][j - 1]  # 왼쪽에서 오는 경우
            dp[i][j] %= 1_000_000_007  # 큰 수 방지

    return dp[n][m]  # 학교 위치의 경로 개수 반환
