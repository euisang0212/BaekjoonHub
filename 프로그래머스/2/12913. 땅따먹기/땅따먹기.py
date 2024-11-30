def solution(land):
    # 초기 dp 배열은 첫 번째 행과 동일
    dp = land[0]
    
    # 각 행에 대해 반복
    for i in range(1, len(land)):
        # 현재 dp 값을 저장하기 위한 임시 배열
        new_dp = [0] * 4
        for j in range(4):
            # 현재 열을 제외한 이전 dp 값 중 최대값을 더함
            new_dp[j] = land[i][j] + max(dp[k] for k in range(4) if k != j)
        # dp 갱신
        dp = new_dp
    
    # 마지막 dp 배열에서 최대값 반환
    return max(dp)
