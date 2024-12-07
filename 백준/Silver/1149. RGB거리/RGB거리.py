def min_cost_to_paint_houses(N, costs):
    dp = [[0] * 3 for _ in range(N)]
    
    # 초기값 설정
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]
    
    # DP를 이용한 최소 비용 계산
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    # 모든 집을 칠하는 최소 비용 출력
    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])

# 입력 처리
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(min_cost_to_paint_houses(N, costs))
