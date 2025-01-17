def solution(triangle):
    # 삼각형의 마지막 행부터 시작하여 위로 올라가며 최대 경로 합 계산
    for i in range(len(triangle) - 2, -1, -1):  # 아래에서 위로
        for j in range(len(triangle[i])):  # 각 행의 모든 열
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    # 꼭대기에 최댓값이 저장됨
    return triangle[0][0]

"""
    for i in range(len(triangle) - 2, -1, -1):
    # 마지막에서 두 번째 행부터 시작하여 위로 올라감
    # i = 현재 행

        for j in range(len(triangle[i])):
        # 삼각형의 한 행에서, 그 행의 모든 요소(열)를 순회하며 값을 업데이트

            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            # 현재 위치([i],[j])에 아래층의 가능한 두 경로 중 최대값을 더함

    return triangle[0][0]
    # 꼭대기에 저장된 최대값 리턴
"""