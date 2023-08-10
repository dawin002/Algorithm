""" 1209 : Sum """

# 100*100 배열에서 가로, 세로, 가장 긴 대각선의 sum을 구하고 최대값 출력

""" my solution """

T = 10
for _ in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # n 열 최대값 구하기
    max_n = max([sum(a) for a in arr])

    # m 행 최대값 구하기
    m_arr = [0] * 100
    for i in range(100):
        for j in range(100):
            m_arr[j] += arr[i][j]
    max_m = max(m_arr)

    # m 행 최대값 구하기 다른 방법(더 좋음)
    # for i in range(100):
    #     temp.append(sum([data[x][i] for x in range(100)]))

    # right down 대각선 합 구하기
    sum_rd = sum([arr[i][i] for i in range(100)])

    # right up 대각선 합 구하기
    sum_ru = sum([arr[99-i][i] for i in range(100)])

    print(f"#{test_case}", max(max_n, max_m, sum_rd, sum_ru))

