""" BFS/DFS : 16. 연구소 """

# 연구소 크기 : N x M ( 3 <= N, M <= 8 )
# 연구소 : 빈칸 / 벽
# 일부 칸 바이러스 존재
# 바이러스 상하좌우 인접 칸 퍼져나감
# 벽 추가로 3개 세워야함
# 0: 빈칸, 1: 벽, 2: 바이러스 ( 2 <= 바이러스 <= 10 , 3 <= 빈칸 )

def new_sol():
    from itertools import combinations
    import copy
    from collections import deque
    n, m = map(int, input().split())
    mmap = [list(map(int, input().split())) for _ in range(n)]
    viruses = []
    blanks = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(m):
            if mmap[i][j] == 0:
                blanks.append((i, j))
            elif mmap[i][j] == 2:
                viruses.append((i, j))
    max_safe = 0
    for comb in combinations(blanks, 3):
        q = deque()
        tmap = copy.deepcopy(mmap)
        for x, y in comb:
            tmap[x][y] = 1
        for x, y in viruses:
            q.append((x, y))
        while q:
            x, y = q.pop()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and tmap[nx][ny] == 0:
                    q.append((nx, ny))
                    tmap[nx][ny] = 2
        safe_count = 0
        for i in range(n):
            for j in range(m):
                if tmap[i][j] == 0:
                    safe_count += 1
        max_safe = max(max_safe, safe_count)

    print(max_safe)

new_sol()




import time

""" my solution """

def print_lab(lab):
    print()
    for line in lab:
        print(' '.join(map(str, line)))
def laboratory():
    import copy
    from itertools import combinations

    # 입력 받기
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    start_time = time.time()

    # 바이러스 이동방향 (상하좌우)
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 최대값 구하는 문제이므로 answer = 최소값 0
    answer = 0

    safe = []  # 초기 안전구역 좌표 리스트
    virus = []  # 초기 바이러스 좌표 리스트
    # 안전구역, 바이르스 좌표 구하기
    for x in range(n):
        for y in range(m):
            cell = lab[x][y]
            if cell == 2:
                virus.append([x, y])
            elif cell == 0:
                safe.append([x, y])

    # 벽 3개 세우는 있는 연구실 조합 전체 확인
    for wall_list in list(combinations(safe, 3)):

        new_lab = copy.deepcopy(lab)
        # 벽 세우기
        for wall in wall_list:
            new_lab[wall[0]][wall[1]] = 1

        # 바이러스 채우기 (DFS)
        stack = copy.deepcopy(virus)
        while stack:
            vir = stack.pop()
            # 바이러스 이동할 수 있는 4방향 좌표 확인
            for dir in direction:
                nx = vir[0] + dir[0]
                ny = vir[1] + dir[1]
                # 연구실 구역 벗어나면 continue
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                # 벽이 아니면 맵에 바이러스 표시, 스택에 새로운 바이러스 좌표 추가
                if new_lab[nx][ny] == 0:
                    new_lab[nx][ny] = 2
                    stack.append([nx, ny])

        # 안전구역 확인
        count = 0
        for line in new_lab:
            for cell in line:
                if cell == 0:
                    count += 1

        # 안전구역 최대값 갱신
        # if answer < count:
            # print_lab(new_lab)  # 바이러스 확산 후 연구실 출력
            # print(count)
        answer = max(answer, count)

    # print()
    print(answer)
    print(f'ex_time : {time.time() - start_time} sec')

# laboratory()

# input1
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# input2
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# input3
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0


""" answer solution ( 백준에서 돌리면 시간초과.. ㅋㅋ ) """

# 차이 나는 부분

# 바이러스 채우기 방식
# 내 풀이 : stack이 빌 때까지 stack에서 바이러스 하나씩 뽑으면서 stack에 새롭게 추가된 바이러스 계속 넣어줌
# 책 풀이 : 재귀함수 이용해서 바이러스 갈 수 있으면 다시 바이러스 확산 함수 호출

# 벽 세우는 방식
# 내 풀이 : combinations(조합) 이용해 벽 세울 수 있는 좌표 3개씩 구해서 세움
# 책 풀이 : DFS 이용. 새로 세운 벽 개수 count로 확인하며 하나씩 세웠다 지웠다 함

def laboratory_ans():
    n, m = map(int, input().split())
    data = []  # 초기 맵 리스트
    temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

    for _ in range(n):
        data.append(list(map(int, input().split())))

    start_time = time.time()

    # 4가지 이동 방향 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = [0]

    # DFS 이용해 각 바이러스가 사방으로 퍼지게 하기
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if temp[nx][ny] == 0:
                    # 해당 위치에 바이러스 배치 후 재귀적으로 수행
                    temp[nx][ny] = 2
                    virus(nx, ny)

    # 안전영역 크기 계산 함수
    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        return score

    # DFS 이용해 울타리 설치하면서 매번 안전 영역의 크기 계산
    def dfs(count, result):
        # 벽이 3개 설치된 경우
        if count == 3:
            # 연구실 temp로 복사
            for i in range(n):
                for j in range(m):
                    temp[i][j] = data[i][j]
            # 각 바이러스의 위치에서 전파 진행
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)
            # 안전 구역의 최댓값 계산
            result[0] = max(result[0], get_score())
            return
        # 빈 공간에 벽 설치
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count, result)
                    data[i][j] = 0
                    count -= 1

    dfs(0, result)
    print(result[0])
    print(f'ex_time : {time.time() - start_time} sec')

# laboratory_ans()