""" 실전 문제 3 : 게임 개발 """
# page 118

# 문제
# 맵 크기 N * M
# 각 칸은 육지 또는 바다
# 각 칸 : (A, B) 좌표의 의미
# A : 북쪽으로부터 떨어진 칸의 개수
# B : 서쪽으로부터 떨어진 칸의 개수

# 캐릭터는 동서남북 중 한쪽 바라봄
# 캐릭터 이동 : 동서남북 중 하나, 바다는 못감
# 이동 매뉴얼
# 1. 현재 방향 기준 왼쪽방향(반시계 90도)부터 갈 칸 정함
# 2. 안가본칸이면 가본다, 가본칸이면 한번더 왼쪽본다
# 3. 4방향 다 가본칸 or 바다면 원래 방향으로 돌아가고 뒤로 한칸 가기
# 4. 뒤쪽 방향이 바다 칸이면 움직임 멈추기

# 입력
# 첫째 줄 : 맵크기 : 4 4
# 둘째 줄 : 캐릭터 위치 & 방향 : 1 1 0 (1,1 좌표에 북쪽 바라봄(0123:북동남서))
# 셋째 줄 ~ : 맵 (바다 : 1 , 육지 : 0)

# 출력
# 이동을 마친 캐릭터가 방문한 칸의 수

# 입력 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

#
""" my code (이동 과정 나오게) """


def makeGame():
    import sys
    input = sys.stdin.readline

    map_row, map_col = map(int, input().rstrip().split())
    cha_now = list(map(int, input().rstrip().split()))
    cha_next = [cha_now[0], cha_now[1]]
    gMap = [list(map(int, input().rstrip().split())) for x in range(map_row)]

    count = 1
    gMap[cha_now[0]][cha_now[1]] = 2

    while True:

        # turn left
        turn_count = 0
        for i in range(4):
            turn_count += 1
            cha_next[0] = cha_now[0]
            cha_next[1] = cha_now[1]

            if cha_now[2] > 0:
                cha_now[2] -= 1
            else:
                cha_now[2] = 3

            if cha_now[2] == 0:
                cha_next[0] -= 1
            elif cha_now[2] == 1:
                cha_next[1] += 1
            elif cha_now[2] == 2:
                cha_next[0] += 1
            elif cha_now[2] == 3:
                cha_next[1] -= 1
            print('t_count :', turn_count, ', cha_now :', cha_now, ', cha_next :', cha_next)

            if gMap[cha_next[0]][cha_next[1]] == 0:
                flag = 'go'
                print('Flag : go')
                break

            if turn_count == 4:
                flag = 'goback'
                print('Flag : go back')

        # go
        if flag == 'go':
            cha_now[0] = cha_next[0]
            cha_now[1] = cha_next[1]
            gMap[cha_now[0]][cha_now[1]] = 2
            count += 1
            # print
            print()
            print('Go :', cha_now)
            for i in range(map_row):
                print(gMap[i])

        # go back
        elif flag == 'goback':
            cha_next[0] = cha_now[0]
            cha_next[1] = cha_now[1]

            if cha_now[2] == 0:
                cha_next[0] += 1
            elif cha_now[2] == 1:
                cha_next[1] -= 1
            elif cha_now[2] == 2:
                cha_next[0] -= 1
            elif cha_now[2] == 3:
                cha_next[1] += 1

            if gMap[cha_next[0]][cha_next[1]] == 1:
                print()
                print('Stop! :', cha_now)
                for i in range(map_row):
                    print(gMap[i])

                print('과정 나오게 출력한 예시')
                break

            else:
                cha_now[0] = cha_next[0]
                cha_now[1] = cha_next[1]
                # print
                print()
                print('Go Back :', cha_now)
                for i in range(map_row):
                    print(gMap[i])

    print(count)


# 4 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 1 0 1 1
# 1 1 1 1 1


#
""" answer code """


def makeGame_3():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().rstrip().split())
    x, y, d = map(int, input().rstrip().split())
    gmap = [list(map(int, input().rstrip().split())) for _ in range(n)]

    dir = ['N', 'E', 'S', 'W']
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0, -1]
    count = 1
    t_count = 0
    gmap[x][y] = 2

    while True:
        t_count += 1
        if d > 0:
            d -= 1
        else:
            d = 3

        nx = x + dx[d]
        ny = y + dy[d]

        if gmap[nx][ny] == 0:
            x = nx
            y = ny
            gmap[x][y] = 2
            count += 1
            t_count = 0
            print('\nGo Forward!')
            print()
            print(x, y, dir[d])
            for i in range(n):
                print(*gmap[i])

        elif t_count == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            t_count = 0

            if gmap[nx][ny] != 1:
                x = nx
                y = ny
                print('\nGo Backward!')
                print()
                print(x, y, dir[d])
                for i in range(n):
                    print(*gmap[i])

            else:
                print('\nStop!')
                print()
                print(x, y, dir[d])
                for i in range(n):
                    print(*gmap[i])
                print()
                print(count)
                break

# 7 7
# 1 1 0
# 1 1 1 1 1 1 1
# 1 0 1 0 1 1 1
# 1 0 0 0 0 0 1
# 1 1 1 0 1 0 1
# 1 1 1 0 1 1 1
# 1 1 1 0 0 0 1
# 1 1 1 1 1 1 1