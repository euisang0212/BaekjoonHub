def solution(clothes):
    answer = 0
    kind_list = []
    for c in clothes: 
        kind_list.append(c[1])
    print(kind_list)

    kind_dict = {}
    for i in kind_list:
        kind_dict[i] = kind_list.count(i)
    print(kind_dict)
    
    answer = 1
    for i in kind_dict.values():
        answer = answer * (i+1)
    answer -= 1
    
    return answer