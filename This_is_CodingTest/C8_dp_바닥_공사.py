""" DP : 바닥 공사 """

""" my code """

starttime = 1810
timeLimit = 20


def floorFix():
    n = int(input())
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 796796

    for i in range(1, n + 1):
        print(f'{i} : {dp[i]}')

    print(dp[n])


# floorFix()


""" 
    바닥공사류 중 어려운 문제들
    
    BOJ 2133 타일 채우기 
    
    점화식 안에 시그마 들어감.. 개어렵
"""


# Nx3 바닥 채워야함
# 2x1, 1x2 타일로 채움
# 가능한 경우의 수 구하기

def fillFloor_3():
    n = int(input())
    maxN = max(n, 4)
    dp = [0] * (maxN + 1)
    dp[0] = 1  # 3x0 floor (채우는 경우의 수 1 : 아무 것도 안놓은 경우)
    dp[1] = 0  # 3x1 floor (못채움)
    dp[2] = 3  # 3x2 floor
    # 아래 두 문장 맞음, 넣어도 됨, 굳이 필요 없어서 뺌
    # dp[3] = 0   # 3x3 floor (못채움)
    # dp[4] = 11  # 3x4 floor
    for i in range(4, n + 1, 2):
        dp[i] = 3 * dp[i - 2]
        for j in range(4, i + 1, 2):
            dp[i] += 2 * dp[i - j]
    print(dp[n])
    # print(dp)


# fillFloor_3()


def fillFloor_3_1():
    n = int(input())
    d = [0] * (n + 1)

    def dp(x):
        if x == 0:
            return 1
        if x == 1:
            return 0
        if x == 2:
            return 3
        if d[x] != 0:
            return d[x]
        res = 3 * dp(x - 2)
        for i in range(3, x + 1):
            if i % 2 == 0:
                res += 2 * dp(x - i)
        d[x] = res
        return d[x]

    print(dp(n))
    # print(d)


# fillFloor_3_1()


""" 
    바닥공사류 중 어려운 문제들

    BOJ 14852 타일 채우기 3 
"""


# 별로 안좋은 알고리즘 : 0 ~ n-3번 까지의 dp값을 계속 더해야해서 dp쓰는데도 오래걸림
# 해결방법 : 다음 코드

def fillFloor_4():
    n = int(input())
    maxN = max(n, 2)
    dp = [0] * (maxN + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n + 1):
        dp[i] = 2 * dp[i - 1] + 3 * dp[i - 2]
        for j in range(3, i + 1):
            dp[i] += 2 * dp[i - j]
        dp[i] %= 1000000007
    print(dp[n])
    # print(dp)


# fillFloor_4()

# 2차원 dp로 0 ~ n-2 까지의 dp값 합도 dp[n][1]에 저장하고 넘어감

def fillFloor_4_2():
    n = int(input())
    maxN = max(n, 2)
    dp = [[0, 0] for i in range(maxN + 1)]
    dp[0][0] = 0
    dp[1][0] = 2
    dp[2][0] = 7
    dp[2][1] = 1

    for i in range(3, n + 1):
        dp[i][1] = (dp[i - 1][1] + dp[i - 3][0]) % 1000000007
        dp[i][0] = (2 * dp[i - 1][0] + 3 * dp[i - 2][0] + 2 * dp[i][1]) % 1000000007
    print(dp[n][0])
    # print(dp)


# fillFloor_4_2()


# 2차원 dp를 변수 5개로 줄여서 만들어보면 더 빠르지 않을까?


""" my code """


def fillFloor_4_3():
    n = int(input())
    ans = [0, 2, 7]
    if n < 3:
        print(ans[n])
        return
    first, second, third = ans
    preSum = 1

    for i in range(3, n + 1):
        preSum = (preSum + first) % 1000000007
        new_third = (2 * third + 3 * second + 2 * preSum) % 1000000007
        first = second
        second = third
        third = new_third
    print(third)


fillFloor_4_3()


def fillFloor_4_4():
    M = 1000000007
    ans = [0, 2, 7]
    N = int(input())
    if N < 3: return ans[N]

    cnt, cross = 2, 1
    a, b, c = ans
    while cnt < N:
        new_c = (2 * cross + 3 * b + 2 * c) % M
        a, b, c = b, c, new_c
        cnt += 1
        cross += a
        cross %= M

    return c


print(fillFloor_4_4())
