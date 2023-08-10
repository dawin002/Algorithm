""" DP 문제 : 31. 금광 """

# n x m 크기 금광
# 각 칸 특정 크기의 금
# 1열, 원하는 행부터 채굴 시작
# 이동 방향 : m번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 중 한가지 선택
# 채굴자가 얻을 수 있는 최대 금 크기 출력

""" my solution """

# 각 칸에서 전 칸의 선택지 중 가져올 수 있는 최대값을 가져와 현재 칸의 값과 더한 뒤 현재 칸에 저장
# 가장 끝 열에 도달하면 최대값 반환

# 개선점
# 1. 2차원 리스트 한 줄로 입력됐을 때 리스트에 넣는 방식
# 2. dp 테이블과 원본 테이블 굳이 구분 안하고 하나의 dp 테이블에 원본 데이터 받아서 수정해도 됨
# 3. 범위 벗어나는 열 체크 방식
#       나는 i==0 이면 (왼, 왼아래) 로 , i==n-1 이면 (왼위, 왼) 으로,
#       둘 다 아니면 (왼위, 왼, 왼아래) 로 범위 직접 지정
#       책은 i==0 이면 left_up = 0, 아니면 left_up = 왼위 ,
#       i==n-1 이면 left_down = 0, 아니면 left_down = 왼아래,
#       left = 왼쪽 으로 받아오고 다 받아온 다음에 max(left_up, left, left_down)
#       ==> 내 방식이 max() 함수 안에 직접 범위 지정하고 max() 함수를 세 번 적어야해서 덜 직관적?

def get_gold():
    n, m = map(int, input().split())
    inp = list(map(int, input().split()))

    gmap = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            gmap[i].append(inp[i * m + j])

    dp = [[0] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = gmap[0][j]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[0][j], dp[1][j]) + gmap[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[-2][j], dp[-1][j]) + gmap[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j], dp[i + 1][j]) + gmap[i][j]

    max_gold = max(dp[:][-1])

    return max_gold


def solution():
    test_case = int(input())
    for _ in range(test_case):
        result = get_gold()
        print(result)

solution()

""" answer get_gold() function : """

def get_gold_ans():
    for tc in range(int(input())):
        n, m = map(int, input().split())
        array = list(map(int, input().split()))

        dp = []
        index = 0
        for i in range(n):
            dp.append(array[index:index+m])
            index += m

        for j in range(1, m):
            for i in range(n):
                # 왼쪽 한 열 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = dp[i-1][j-1]
                # 왼쪽 한 열 아래에서 오는 경우
                if i == n-1:
                    left_down = 0
                else:
                    left_down = dp[i+1][i-1]
                # 왼쪽 같은 열에서 오는 경우
                left = dp[i][j-1]
                # dp에 3 방향의 값 중 최대값 더하기
                dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        result = 0
        for i in range(n):
            result = max(result, dp[i][m-1])

        print(result)

# input1
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
