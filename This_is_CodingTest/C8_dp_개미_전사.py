""" DP : 개미 전사 """

""" my code """

# 히히 내가 풀어서 맞춤
# 두 개만 고려하면 됨
# i-1번째 창고를 털면 i번째 창고를 못털고
# i-2번째 창고를 털면 i번째 창고도 털수있음
# 따라서 점화식은
# DP[i] = max ( DP[i-1] , DP[i-2] + Arr[i] )

def antWarrior() :
    # n = int(input())
    # arr = list(map(int, input().split()))
    arr = [1, 3, 1, 5, 10, 11, 100]
    n = len(arr)

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
        # print(dp)

    print(dp[-1])

antWarrior()
