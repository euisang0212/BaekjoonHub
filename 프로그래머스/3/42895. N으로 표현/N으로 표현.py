def solution(N, number):
    if N == number:
        return 1

    # DP 테이블 초기화 (1 ~ 8 사용 가능)
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 연속 사용한 숫자 추가

    # 동적 프로그래밍
    for i in range(1, 9):  # N 사용 횟수
        for j in range(1, i):  # i를 두 부분으로 나누어 조합
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)  # 덧셈
                    if x - y > 0:  # 음수와 0 제외
                        dp[i].add(x - y)
                    dp[i].add(x * y)  # 곱셈
                    if y != 0:  # 나눗셈에서 분모가 0이 아닌 경우
                        dp[i].add(x // y)

        # 목표 숫자 확인
        if number in dp[i]:
            return i

    return -1  # 8번 이상 사용해도 목표 숫자를 만들 수 없으면 -1
