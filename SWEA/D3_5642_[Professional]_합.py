""" 5642. [Professional] 합 """

# 주어진 수열의 연속된 부분수열 중 sum(부분수열)의 최대값 찾기

""" my solution """

# 2차원 리스트 dp 로 만들었는데 동작은 하나 입력값이 10만개라 메모리 초과

def sum_dp_failed():

    n = int(input())
    arr = list(map(int, input().split()))
    # print(f"arr : {arr}")

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[0][i] = arr[i-1]

    for i in range(1, n+1):
        for j in range(i, n+1):
            dp[i][j] = dp[i][j-1] + arr[j-1]

    max_res = -int(1e9)

    for i in range(1, n+1):
        max_res = max(max_res, max(dp[i][i:n+1]))
    #     print(dp[i][i:n+1])
    #
    # for d in dp:
    #     print(d)

    return max_res

# print(sum_dp_failed())

""" answer solution : sum add arr[i], check max """

# 리스트 0번부터 순차탐색
# sum_value 변수에 += 연산 하면서 max_value 갱신
# sum_value 값이 음수가 되면 0으로 초기화 후 다음 원소 탐색
# 특징 : 변수 하나에 부분연속수열 더한값 저장, 비교

def sum_ans():
    T = int(input())
    for TC in range(1, T + 1):
        N = int(input())
        Arr = list(map(int, input().split()))
        # 최대값 초기화
        maxV = -1000000
        # 합 초기화
        sumV = 0
        # 시작 인덱스 탐색
        for i in range(N):
            # 처음부터 더하기
            sumV += Arr[i]
            # 최대값 갱신
            if sumV > maxV:
                maxV = sumV
            # 현재까지의 합이 음수이면 버리기
            if sumV < 0:
                sumV = 0
        print("#{} {}".format(TC, maxV))

""" my solution : 실패..!!! """

# 특징 : dp 테이블 직접 갱신하며 max 값 탐색
#       sum 변수 사용하지 않음

def sum_hint():
    t = int(input())
    for tc in range(1, t+1):
        n = int(input())
        dp = list(map(int, input().split()))
        max_val = -int(1e9)

        for i in range(1, n):
            if dp[i] > 0 and dp[i] + dp[i-1] > 0:
                dp[i] += dp[i-1]
            if max_val < dp[i]:
                max_val = dp[i]

        print("#{} {}".format(tc, max_val))

# sum_hint()



# 5
# 7
# 20 -20 10 5 -15 21 3
# 7
# -1 -2 -3 -4 -5 -6 -7
# 7
# -7 -7 -7 -7 -7 -7 -7
# 7
# 1 2 3 4 5 6 7
# 7
# -7 2 -10 4 -2 2 1
