def solution(files):
    # 파일명을 HEAD, NUMBER로 분리하는 함수
    def split_file(file):
        head, number, tail = "", "", ""
        number_found = False
        tail_count = 0

        for char in file:
            if tail_count == 0 and char.isdigit() and not number_found:
                number += char
                number_found = True
            elif char.isdigit() and number_found:
                if len(number) < 5:  # NUMBER는 최대 5자리
                    number += char           
            elif tail_count ==0 and not number_found:
                head += char
            else:
                number_found =False
                tail_count =1
                tail += char

        return head, number, tail

    # 파일 리스트를 정렬 기준에 맞게 변환
    files_split = []
    for file in files:
        head, number, tail = split_file(file)
        files_split.append((head, int(number), file))  # NUMBER를 int로 변환

    # 정렬: HEAD -> NUMBER -> 입력 순
    files_split.sort(key=lambda x: (x[0].lower(), x[1]))

    # 정렬된 결과에서 원본 파일명만 반환
    return [file[2] for file in files_split]