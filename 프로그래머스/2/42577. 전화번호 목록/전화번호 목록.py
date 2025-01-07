"""
# 정렬
def solution(phone_book):
    # 전화번호 목록 정렬
    phone_book.sort()

    # 정렬된 리스트에서 인접한 두 전화번호를 비교
    for i in range(len(phone_book) - 1):
        # 현재 전화번호가 다음 전화번호의 접두사인지 확인
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False  # 접두사가 존재하면 False 반환

    return True  # 모든 전화번호가 서로 접두사 관계가 아닐 때 True 반환
"""

# 해시셋
def solution(phone_book):
    # 전화번호 목록을 해시셋으로 변환
    phone_set = set(phone_book)

    # 모든 전화번호의 접두사를 확인
    for number in phone_book:
        for i in range(1, len(number)):
            # 현재 전화번호의 접두사가 해시셋에 존재하는지 확인
            if number[:i] in phone_set:
                return False  # 접두사가 존재하면 False 반환

    return True  # 모든 전화번호가 서로 접두사 관계가 아닐 때 True 반환




#시간 초과
"""
def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        # 현재 전화번호
        current_number = phone_book[i]
        
        # 나머지 전화번호와 비교
        for j in range(len(phone_book)):
            if i != j:  # 자기 자신은 비교하지 않음
                # 현재 전화번호가 다른 전화번호의 접두사인지 확인
                if phone_book[j].startswith(current_number):
                    return False  # 접두사가 존재하면 False 반환

    
    return answer
"""