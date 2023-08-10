""" DFS/BFS : 18. 괄호 변환 """


""" my solution (failed, 빼먹은 코드 몇 개 있었음) """

def is_balanced(w):
    left, right = 0, 0
    for a in w:
        if a == '(':
            left += 1
        elif a == ')':
            right += 1
    if left == right:
        return True
    else:
        return False

def is_correct(w):
    stack = []
    for a in w:
        if a == '(':
            stack.append('(')
        elif a == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def make_correct_string(w):
    if not w:
        return w
    u, v = "", ""
    for i in range(1, len(w)):
        u, v = w[:i+1], w[i+1:]
        if is_balanced(u):
            break
    if is_correct(u):
        return u + make_correct_string(v)
    else:
        new_v = '('
        new_v += make_correct_string(v)
        new_v += ')'
        u = list(u[1:-1])  # 요소 다뤄야해서 리스트로 바꿔줬다가
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        new_v += ''.join(u)  # 문자열 합쳐야해서 다시 join()으로 바꿔줌
        return new_v  # 이 부분 그냥 u 로 해서 틀린 거였음

def parenthesis():
    w = input()
    w = w[1:-1]
    answer = '"' + make_correct_string(w) + '"'
    print(answer)

parenthesis()

""" answer solution """

# 균형 잡힌 괄호 문자열의 인덱스 반환 (몇 번째 인덱스에서 균형 잡히는지)
def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우 True 반환

def recursion(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # u가 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + recursion(v)
    # u가 올바른 괄호 문자열 아니면 아래 과정 수행
    else:
        answer = '('
        answer += recursion(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer

def parenthesis_ans():
    p = input()
    p = p[1:-1]
    answer = recursion(p)
    print('"' + answer + '"')

# parenthesis_ans()