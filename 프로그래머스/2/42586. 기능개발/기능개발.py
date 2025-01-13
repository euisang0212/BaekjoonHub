"""
def solution(progresses, speeds):
    answer = []
    check_progresses = progresses[:]  # 현재 진행도를 복사
    
    # 1일마다 진행도 갱신
    while check_progresses:
        # 각 작업의 진행도를 갱신
        for i in range(len(check_progresses)):
            check_progresses[i] += speeds[i]  # 각 인덱스에 속도를 더함
        
        count = 0

        # 첫 번째 작업이 100 이상인 경우 확인
        while check_progresses and check_progresses[0] >= 100:
            check_progresses.pop(0)  # 완료된 작업 제거
            count += 1
        
        if count > 0:  # 작업이 완료되었다면
            answer.append(count)  # 완료된 작업 수 추가
    
    return answer
"""

def solution(progresses, speeds):
    answer = []
    days_needed = []  # 각 작업이 완료되는 데 필요한 일수를 저장
    
    # 각 작업이 완료되는 데 걸리는 일수 계산
    for i in range(len(progresses)):
        days = (100 - progresses[i] + speeds[i] - 1) // speeds[i]  # 올림 처리
        days_needed.append(days)

    count = 0  # 배포할 기능의 수
    max_days = days_needed[0]  # 첫 번째 기능의 완료 일수로 초기화

    for days in days_needed:
        if days <= max_days:  # 현재 작업이 max_days 이내에 완성되면
            count += 1  # 카운트 증가
        else:
            answer.append(count)  # 카운트 추가
            count = 1  # 새로운 기능 카운트 초기화
            max_days = days  # max_days 업데이트

    answer.append(count)  # 마지막 카운트 추가
    return answer
