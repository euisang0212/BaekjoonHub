from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # 분모의 최소 공배수 (LCM) 계산
    lcm = (denom1 * denom2) // gcd(denom1, denom2)
    
    # 분자를 공통 분모에 맞게 변환 후 더하기
    new_numer = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
    
    # 분자와 분모를 최대 공약수로 나누어 기약 분수로 변환
    divisor = gcd(new_numer, lcm)
    return [new_numer // divisor, lcm // divisor]
