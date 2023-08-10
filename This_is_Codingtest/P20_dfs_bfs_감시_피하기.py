""" DFS/BFS : 20. 감시 피하기 """

# 생각보다 쉬워보임 근데 왜 60분?

""" my solution """

def avoid_teacher():
    from itertools import combinations

    n = int(input())
    dx_list = [-1, 0, 1, 0]
    dy_list = [0, 1, 0, -1]
    gmap = [list(input().split()) for _ in range(n)]

    t_list = []
    x_list = []

    for i in range(n):
        for j in range(n):
            if gmap[i][j] == 'T':
                t_list.append((i, j))
            elif gmap[i][j] == 'X':
                x_list.append((i, j))

    def find(tx, ty, dx, dy):
        nx = tx + dx
        ny = ty + dy
        if 0 <= nx < n and 0 <= ny < n:
            cell = gmap[nx][ny]
            if cell == 'X':
                return find(nx, ny, dx, dy)
            elif cell == 'T' or cell == 'O':
                return False
            elif cell == 'S':
                return True
        return False

    for comb in combinations(x_list, 3):
        found = False
        for ox, oy in comb:
            gmap[ox][oy] = 'O'

        ### 맵 출력
        # for line in gmap:
        #     print(' '.join(line))
        # print()

        for tx, ty in t_list:
            for i in range(4):
                found = find(tx, ty, dx_list[i], dy_list[i])
                if found:
                    break
            if found:
                break

        if not found:
            print('YES')
            return

        for ox, oy in comb:
            gmap[ox][oy] = 'X'

    print('NO')
    return

avoid_teacher()

# input1
# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# input2
# 4
# S S S T
# X X X X
# X X X X
# T T T X


""" answer solution """

def avoid_teacher_ans():
    from itertools import combinations

    n = int(input())
    board = []
    teachers = []
    spaces = []

    for i in range(n):
        board.append(list(input().split()))
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append((i, j))
            if board[i][j] == 'X':
                spaces.append((i, j))

    def watch(x, y, direction):

        if direction == 0:
            while y >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y -= 1

        if direction == 1:
            while y < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                y += 1

        if direction == 2:
            while x >= 0:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x -= 1

        if direction == 3:
            while x < n:
                if board[x][y] == 'S':
                    return True
                if board[x][y] == 'O':
                    return False
                x += 1

        return False

    # 장애물 설치 후 학생 한 명이라도 감지되는지 검사
    def process():
        for x, y in teachers:
            for i in range(4):
                if watch(x, y, i):
                    return True
        return False

    # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부
    find = False

    for data in combinations(spaces, 3):

        # 장애물 설치
        for x, y in data:
            board[x][y] = 'O'

        # 학생이 한 명도 감지되지 않은 경우
        if not process():
            # 원하는 경우를 발견
            find = True
            break

        # 장애물 회수
        for x, y in data:
            board[x][y] = 'X'

    if find:
        print('YES')
    else:
        print('NO')