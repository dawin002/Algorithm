""" DP : 1로 만들기 """

# 수가 5로 나누어 떨어지면 5로 나눌 것
# 수가 3으로 나누어 떨어지면 3으로 나눌 것
# 수가 2로 나누어 떨어지면 2로 나눌 것
# 수에서 1 뺄 것

# 위 4개 연산 이용해 1 만들건데
# 연산 사용한 횟수의 최소값 구하기

""" my code """


def make_one():
    # x = int(input())
    x = 10
    dp = [0] * (x + 1)

    for i in range(2, x + 1):
        # 현재 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    print('ans =', dp[x])

    for i in range(1, x + 1):
        print(f'{i} : {dp[i]} times')


make_one()
