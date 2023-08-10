""" DP 문제 : 36. 편집 거리 """

# 문자열 A 를 편집하여 문자열 B 로 만들 것
# 편집 연산 3개
# 1. insert  : 특정 위치에 문자 하나 삽입
# 2. remove  : 특정 위치의 문자 하나 삭제
# 3. replace : 특정 위치의 문자 하나 다른 문자로 교체
# 연산 횟수 최소값 구하기

""" answer solution """

# dp 열(세로 인덱스) : [빈칸, 원본 문자열 a 의 각 문자]
# dp 행(가로 인덱스) : [빈칸, 목표 문자열 b 의 각 문자]
# dp 각 칸의 의미 : dp[i][j] = 부분문자열 a[0:i]을 부분문자열 b[0:j]로 바꾸는데 드는 최소 편집 거리

def edit_distance_ans():
    a = input()
    b = input()

    n = len(a)
    m = len(b)

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자 같으면 dp[왼쪽위] 값 dp[현재칸]에 그대로 넣기 (비용 변화 없음)
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자 다르면 아래 3칸 중 최소값 dp[현재칸]에 넣기 (비용 1 증가)
            else:  # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽위) 중 비용 최소값인 칸
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    # 마지막 칸에 최소 비용 저장됨
    print(dp[n][m])

    # 추가로 dp 에 저장된 전체 값 확인
    print(' ', '_', ' '.join(list(b)))
    for i in range(n+1):
        if i == 0:
            print('_', end=' ')
        else:
            print(a[i-1], end=' ')
        print(' '.join(map(str, dp[i])))
    # dp :  _ s a t u r d a y
    #     _ 0 1 2 3 4 5 6 7 8
    #     s 1 0 1 2 3 4 5 6 7
    #     u 2 1 1 2 2 3 4 5 6
    #     n 3 2 2 2 3 3 4 5 6
    #     d 4 3 3 3 3 4 3 4 5
    #     a 5 4 3 4 4 4 4 3 4
    #     y 6 5 4 4 5 5 5 4 3

edit_distance_ans()

# input
# sunday
# saturday


""" my solution : 실패 (두 문자열의 공통된 서브 문자열 길이 최소값까지 밖에 못 구함) """

def edit_distance():
    a = list(input())
    b = list(input())

    dp = [[0]*len(b) for _ in range(len(a))]
    for j in range(len(b)):
        if a[0] == b[j]:
            dp[0][j] = 1

    for i in range(1, len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if j == 0:
                    dp[i][j] = 1
                else:
                    for k in range(i-1, -1, -1):
                        for l in range(j-1, -1, -1):
                            if dp[k][l] != 0:
                                dp[i][j] = dp[k][l] + 1
                                break
                        if dp[i][j] != 0:
                            break
                    else:
                        dp[i][j] = 1

    for line in dp:
        print(' '.join(map(str, line)))

# edit_distance()
