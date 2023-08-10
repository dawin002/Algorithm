""" DFS/BFS 문제 : 19. 연산자 끼워 넣기 """



""" my solution : 완탐 + set(permutation) 으로 풀었는데 dfs 로 풀면 시간복잡도 훨씬 낮음 """

# start time = 20:18

# 이게 완탐 말고 다른 방식으로 풀린다고??

def insert_operator():
    from itertools import permutations
    n = int(input())
    arr = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    oper_list = []

    def plus(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def division(a, b):
        if a < 0 and b < 0:
            return -a // -b
        elif a < 0 and b > 0:
            return -(-a // b)
        elif a > 0 and b < 0:
            return -(a // -b)
        else:
            return a // b

    for i in range(len(operator)):
        oper_list += [i] * operator[i]

    print(f"oper_list = {oper_list}")

    max_ans = int(-1e9)
    min_ans = int(1e9)

    for oper in set(permutations(oper_list)):
        result = arr[0]
        for i in range(len(oper)):
            if oper[i] == 0:
                result = plus(result, arr[i+1])
            elif oper[i] == 1:
                result = minus(result, arr[i+1])
            elif oper[i] == 2:
                result = multiply(result, arr[i+1])
            elif oper[i] == 3:
                result = division(result, arr[i+1])
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)

    print(max_ans)
    print(min_ans)

# insert_operator()

# input1
# 2
# 5 6
# 0 0 1 0

# input2
# 3
# 3 4 5
# 1 0 1 0

# input3
# 6
# 1 2 3 4 5 6
# 2 1 1 1


""" answer solution : dfs 이용 풀이 방식 """

""" 소감 : 어렵다... 하지만 알아 둬야 하겠지?? """

# global 써야해서 함수로 정의 x

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최소값 최대값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대해 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1

# DFS 함수 호출
dfs(1, data[0])

# 최대값 최소값 출력
print(max_value)
print(min_value)