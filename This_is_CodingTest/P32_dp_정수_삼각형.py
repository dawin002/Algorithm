""" DP 문제 : 32. 정수 삼각형 """

""" my solution """

def int_triangle():
    n = int(input())
    dp = []
    for i in range(n):
        dp.append(list(map(int, input().split())))

    for i in range(1, n):
        dp[i][0] += dp[i-1][0]
        for j in range(1, len(dp[i])-1):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        dp[i][-1] += dp[i-1][-1]

    result = max(dp[n-1])
    print(result)

# int_triangle()


""" my solution 2 : 이 전 문제 풀이 방식 (좀 더 김), 정확히 정답과 동일 """

def int_triangle_2():
    n = int(input())
    dp = []
    for i in range(n):
        dp.append(list(map(int, input().split())))

    for i in range(1, n):
        m = i + 1
        for j in range(m):
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if j == m-1:
                right_up = 0
            else:
                right_up = dp[i-1][j]

            dp[i][j] = dp[i][j] + max(left_up, right_up)

    result = max(dp[n-1])
    print(result)

int_triangle_2()

# input1
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5