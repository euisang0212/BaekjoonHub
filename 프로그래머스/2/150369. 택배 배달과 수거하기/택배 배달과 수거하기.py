from math import ceil

def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_remain = 0
    pickup_remain = 0

    # 뒤에서부터 탐색
    for i in range(n - 1, -1, -1):
        delivery_remain += deliveries[i]
        pickup_remain += pickups[i]

        # 현재 위치에서 필요한 왕복 수 계산
        while delivery_remain > 0 or pickup_remain > 0:
            trips = max(ceil(delivery_remain / cap), ceil(pickup_remain / cap))
            answer += (i + 1) * 2 * trips

            # 현재 왕복으로 처리한 상자만큼 빼기
            delivery_remain -= cap * trips
            pickup_remain -= cap * trips

    return answer
