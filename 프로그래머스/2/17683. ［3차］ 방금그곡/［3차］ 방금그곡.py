def solution(m, musicinfos):
    answer = "(None)"  # 기본값 설정
    max_duration = 0  # 가장 긴 재생 시간 저장

    # 음표 변환 함수
    def convert_notes(notes):
        return (notes
                .replace("C#", "c")
                .replace("D#", "d")
                .replace("F#", "f")
                .replace("G#", "g")
                .replace("A#", "a")
                .replace("B#", "b")
               )

    m = convert_notes(m)  # 입력된 멜로디 변환

    for musicinfo in musicinfos:
        # 데이터를 ',' 기준으로 분리
        s, e, title, melody = musicinfo.split(",")
        melody = convert_notes(melody)  # 악보 변환
        
        # 시간 계산
        start_hour, start_min = map(int, s.split(":"))
        end_hour, end_min = map(int, e.split(":"))
        duration = (end_hour * 60 + end_min) - (start_hour * 60 + start_min)
        
        # 재생 시간에 따라 악보 반복 생성
        full_music = melody * (duration // len(melody)) + melody[:duration % len(melody)]
        
        # 멜로디가 악보에 포함되는지 확인
        if m in full_music:
            # 재생 시간이 더 길거나, 동일한 경우 먼저 입력된 곡을 선택
            if duration > max_duration:
                max_duration = duration
                answer = title

    return answer
