# 1번 ~ n번 집
# 빨/초/파 중 하나로 집 칠하기
# 각 집 빨,초,파 칠하는 가격 다름
# 모든 집 칠하는 비용의 최소값
# 규칙 : 모든 집은 이웃한 집과 색이 달라야함

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e9) for _ in range(3)] for _ in range(n)]


def recur(idx, color):
    # print('now :', idx, color)

    if idx == n:
        # print('idx end return')
        return 0

    # if color > -1:
    #     if dp[idx][color] != int(1e9):
    #         return dp[idx][color]
    # 내 밑에 색중에 나 말고 다른 색 두개 색이 픽스된 경우(1e9 아닐때) 디피 나 리턴

    mini = int(1e9)

    for i in range(3):
        if i == color:
            continue
        dp[idx][i] = min(dp[idx][i], recur(idx+1, i)+arr[idx][i])
        # print(dp)
        mini = min(mini, dp[idx][i])
    # print('return :', mini)

    return mini

recur(0, 0)
recur(0, 1)
recur(0, 2)

print(min(dp[0]))
# print(dp)

# 3
# 26 40 83
# 49 60 57
# 13 89 99
