""" 1018 : 체스판 다시 칠하기 """

# 체스판 만들기
# 무작위로 흰검 칠해진 큰 판에서 떼어내서 덧칠할 것
# 큰 판에서 8*8 칸 고를 때 칠해야 할 칸 수 최소값 구하기

""" my solution """

def paint_chess_board():
    w_first = []
    b_first = []
    for i in range(8):
        if i % 2 == 0:
            w_first.append(['W', 'B'] * 4)
            b_first.append(['B', 'W'] * 4)
        else:
            w_first.append(['B', 'W'] * 4)
            b_first.append(['W', 'B'] * 4)

    n, m = map(int, input().split())
    min_res = 65
    cmap = [list(input()) for _ in range(n)]

    for start_n in range(n-8+1):
        for start_m in range(m-8+1):
            w_res = b_res = 0
            for i in range(8):
                for j in range(8):
                    if cmap[start_n + i][start_m + j] != w_first[i][j]:
                        w_res += 1
                    if cmap[start_n + i][start_m + j] != b_first[i][j]:
                        b_res += 1
                if min_res <= min(w_res, b_res):
                    break
            min_res = min(min_res, w_res, b_res)

    print(min_res)

paint_chess_board()