""" 구현 문제 : 11. 뱀 """

""" 나중에 다시 풀어볼 것 : 25분 초과 """

# 사과 먹으면 뱀 길이 += 1
# 벽이나 몸에 박으면 게임 오버
# N x N 정사각 보드
# 뱀 시작 위치 = (1,1)
# 뱀 시작 길이 = 1
# 첫 이동 방향 = 오른쪽
# 매초 이동
# 이동 규칙 - 뱀은 몸 길이를 늘려 머리를 다음칸에 위치
#         - 다음 칸에 사과가 있다면 사과 없어지고 꼬리 움직이지 않음
#         - 다음 칸에 사과가 없다면 몸 길이 줄여 꼬리 있던 칸 비움
#
# 입력 조건 - 첫줄 보드 길이 N
#         - 다음줄 사과 개수 K
#         - 다음 K개 줄에 사과 위치
#         - 다음 줄 뱀 방향 변환 횟수 L
#         - 다음 L개 줄에 뱀 방향 변환 정보 X(X초 후 방향 변환), C('L':왼쪽, 'D':오른쪽)
#
# 출력 조건 - 첫째 줄에 몇 초에 게임 오버 인지 출력

""" my code """

def print_snake(time, board):
    print(f'time={time}')
    b = len(board)
    for i in range(1, b):
        print(*board[i][1:])
    print()

def snake():
    from collections import deque

    # 보드 만들기
    n = int(input())
    board = [[0] * (n + 1) for _ in range(n + 1)]  # blank = 0

    # 보드에 사과 넣기
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 2  # apple = 2

    # 방향전환시간, 전환방향 받기
    l = int(input())
    order = []
    for _ in range(l):
        inp = input().split()
        x, c = int(inp[0]), inp[1]
        order.append((x, c))

    # 오른쪽->아래->왼쪽->위 (시계방향) 순서로 이동방향 표 만들기
    dir_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽으로 회전

    # 초기값 설정

    x, y = 1, 1      # 뱀 시작 좌표
    board[x][y] = 1  # 보드에 뱀 놓기
    dir = 0          # 현재 방향 : 0 (오른쪽)
    now = 0          # 현재 방향전환 순서 : 0 (8, 'D')
    time = 0         # 경과 시간

    # 뱀 몸 전체 좌표 (꼬리 추적용)
    snake = deque()
    snake.append((1, 1))

    while True:
        print_snake(time, board)  # 보드 출력

        time += 1

        # 뱀 다음 좌표 확인
        nx = x + dir_arr[dir][0]
        ny = y + dir_arr[dir][1]

        # 화면 밖으로 나가면 or 자기 몸통 만나면
        if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 1:
            print(time)
            return

        # 앞으로 갈 수 있으면
        else:
            # 사과 없을 때는 꼬리칸 지우기, 뱀 길이 1칸 줄이기
            if board[nx][ny] == 0:
                tail_x, tail_y = snake.popleft()
                board[tail_x][tail_y] = 0

            # 뱀 머리 이동, 뱀 길이 1칸 늘리기
            board[nx][ny] = 1
            snake.append((nx, ny))
            x, y = nx, ny

        # 현재 시간 == 방향전환 시간 현재값  되면 머리 방향 바꿔주기
        # now 가 l을 넘으면 무시 (그 뒤로는 방향 전환이 없어서)
        if now < l and order[now][0] == time :
            if order[now][1] == 'D':
                dir = (dir + 1) % 4
            elif order[now][1] == 'L':
                dir = (dir - 1) % 4
            else:
                print(f"ERROR : dir = '{dir}'")
                return
            now += 1

snake()

# input 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# input 2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# input 3
# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L