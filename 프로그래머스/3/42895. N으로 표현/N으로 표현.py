def solution(N, number):
    if N == number:
        return 1

    # DP 테이블 초기화
    dp = [set() for _ in range(9)]  # dp[i]: N을 i번 사용해서 만들 수 있는 숫자의 집합
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 연속 사용한 숫자 추가 (ex: 5, 55, 555)

    # 동적 프로그래밍 진행
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:  # 0으로 나누는 경우 제외
                        dp[i].add(x // y)
        # 목표 숫자가 현재 집합에 있다면 반환
        if number in dp[i]:
            return i

    # 8번 이상 사용해도 목표 숫자를 못 만들면 -1 반환
    return -1
