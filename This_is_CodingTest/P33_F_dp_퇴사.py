""" DP 문제 : 33. 퇴사 """

# n 일 동안 일함
# 각 날에 저장된 값 : T , P
# T : 이 날 시작한 일의 소요 시간
# P : 이 날 시작한 일의 보수
# n 일 까지만 일을 할 때 벌 수 있는 최대 보수
# 주의 1 : 끝나는 날이 n일이 넘어가는 일은 시작 못함

""" my solution : 답지에서 점화식 보고 품 """

def retire_company():
    n = int(input())
    t = []
    p = []
    dp = [0] * (n+1)
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)

    max_value = 0

    for i in range(n-1, -1, -1):
        if i + t[i] > n:
            dp[i] = max_value
        else:
            max_value = max(dp[i + t[i]] + p[i], max_value)
            dp[i] = max_value

    print(dp)
    print(max_value)

retire_company()

# input1
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# input2
# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10

# input3
# 10
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6
# 5 10
# 5 9
# 5 8
# 5 7
# 5 6

# input4
# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50