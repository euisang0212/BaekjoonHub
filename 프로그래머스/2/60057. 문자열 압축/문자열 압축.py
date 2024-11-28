def compress_string(s, unit):
    compressed = ""
    count = 1  # 반복 카운트
    for i in range(0, len(s), unit):
        # 현재 단위와 다음 단위를 비교
        current = s[i:i + unit]
        next = s[i + unit:i + 2 * unit]
        if current == next:
            count += 1  # 연속된 경우 카운트 증가
        else:
            compressed += (str(count) + current) if count > 1 else current
            count = 1  # 카운트 초기화
    return compressed

def solution(s):
    if len(s) == 1:
        return 1  # 길이가 1인 경우 압축은 불필요

    min_length = len(s)  # 최소 길이 초기화
    for unit in range(1, len(s) // 2 + 1):  # 1개 단위부터 len(s)//2 단위까지
        compressed = compress_string(s, unit)
        min_length = min(min_length, len(compressed))  # 최소 길이 갱신

    return min_length