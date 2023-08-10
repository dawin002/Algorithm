""" DP 효율적인 화폐 구성 """

# n가지 종류 화폐
# 최소한의 개수로 M원 만드는 화폐 개수 찾기
# 개수제한 없음
# 첫째줄 n, m
# 둘째줄~n줄 화폐 종류
# 최소한의 화폐 개수 출력 or 안되면 -1

""" 해설 보고 풀어보자 """

# 1. 점화식 구하기
# 금액 i를 만들 수 있는 화폐 최소 개수 : a
# 화폐의 단위 : k
# 금액 i-k를 만들 수 있는 화폐 최소 개수 : a(i-k)
# 다음 점화식 성립
# a(i-k)를 만들 수 있으면 a(i) = min( a(i), a(i-k)+1 )
# a(i-k)를 만들 수 없으면 a(i) = INF

# 2. 점화식 모든 화폐 단위에 적용
# k 크기 만큼의 리스트 필요
# 각 인덱스 의미 : 금액

def moneyCombin_my() :
    INF = 10001
    # n, m = map(int, input().split())
    # arr = [ int(input()) for _ in range(n)]
    n, m = 3, 500
    arr = [2, 3, 5]
    dp = [INF] * (m+1)
    dp[0] = 0
    for c in arr:
        # print(f'a = {c}')
        for i in range(c, m+1):
            dp[i] = min(dp[i], dp[i-c]+1)
            # dp[i]에 만들어져있는 화폐조합의 개수와
            # dp[i]보다 현재 화폐단위(a)만큼 앞에 있는 dp[i-a]에 1(a 1개)을 더한 개수를 비교해
            # 더 작은 개수를 dp[i]에 갱신한다
            # print(f'i = {i}, dp = {dp}')

    if dp[m] == INF:
        print(-1)
    else:
        print(dp[m])

moneyCombin_my()





def new_coin():
    INF = 1e9
    n, m = 3, 500
    coin = [2, 3, 5]
    dp = [INF] * (m + 1)
    dp[0] = 0 ######################## 중요!!!!
    for c in coin:
        dp[c] = 1
    for i in range(m+1):
        for c in coin:
            if i-c > 0 and dp[i-c] != INF:
                dp[i] = min(dp[i], dp[i-c] + 1)

    print(dp)
    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])

new_coin()
