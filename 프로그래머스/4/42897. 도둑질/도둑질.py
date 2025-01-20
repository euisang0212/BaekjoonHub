def solution(money):
    n = len(money)

    # 첫 번째 집을 터는 경우
    prev1, curr1 = money[0], max(money[0], money[1])
    for i in range(2, n - 1):
        prev1, curr1 = curr1, max(curr1, prev1 + money[i])

    # 첫 번째 집을 털지 않는 경우
    prev2, curr2 = 0, money[1]
    for i in range(2, n):
        prev2, curr2 = curr2, max(curr2, prev2 + money[i])

    return max(curr1, curr2)
