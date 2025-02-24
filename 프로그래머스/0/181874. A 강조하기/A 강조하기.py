def solution(myString):
    answer = []
    
    myString = myString.lower()
    print(myString)
    
    for char in myString:
        answer.append('A' if char == 'a' else char)
    
    return "".join(answer)