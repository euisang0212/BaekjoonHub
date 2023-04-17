# 입력
# 입력 데이터는 표준 입력을 사용한다.
# 입력은 T개의 테스트 데이터로 주어진다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
# 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

# 출력
# 출력은 표준 출력을 사용한다.
# 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”,
# 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

class Stack:
    def __init__(self):
        self.top = []
    
    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []
    
    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('('):
            stack.push(ch)
        elif ch in (')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == ')' and left != '(') :
                    return False
    return stack.isEmpty()

def printResult(string):
    if checkBrackets(string):
        print("YES")
    else:
        print("NO")

num = int(input())
for i in range(num):
    check_data = input()
    printResult(check_data)