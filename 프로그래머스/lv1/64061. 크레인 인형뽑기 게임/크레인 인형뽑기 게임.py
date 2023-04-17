def solution(board, moves):
    answer = 0
    
    result_box = []

    for move_num in moves:
        for line_num in board:
            if line_num[move_num-1] != 0:
                result_box.append(line_num[move_num-1])
                line_num[move_num-1] = 0
                break
        
        # 바구니에 인형이 2개 이상 있는지 확인 후,
        # 바구니에 마지막으로 담긴 인형 2개가 같은 인형일 때 제거 후,
        # 제거한 인형 2개 답에 더해줌
        if len(result_box) >= 2 and result_box[-1] == result_box[-2]:
            answer += 2
            result_box = result_box[:-2]
    
    return answer