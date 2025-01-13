def solution(record):
    answer = []
    
    user_dic = {}
    
    for r in record:
        parts = r.split()
#        print(parts)
        
        cmd = parts[0]
        uid = parts[1]
        
        if cmd == "Enter":
            nickname = parts[2]
            user_dic[uid] = nickname
            answer.append((uid, "님이 들어왔습니다."))
        elif cmd == "Leave":
            answer.append((uid, "님이 나갔습니다."))
        elif cmd == "Change":
            nickname = parts[2]
            user_dic[uid] = nickname

#    print(answer)
    result = [user_dic[uid] + message for uid, message in answer]
    
    return result