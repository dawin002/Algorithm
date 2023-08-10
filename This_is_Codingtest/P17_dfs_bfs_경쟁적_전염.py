""" DFS/BFS : 17. 경쟁적 전염 """

# N x N 시험관 (1, 1) 시작
# 1 ~ K 번 바이러스 존재
# 모든 바이러스 1초마다 상하좌우 증식
# 낮은 번호부터 증식
# 빈칸에만 증식가능
# S 초 지난 후 (X, Y) 칸의 바이러스 출력
# 빈칸이면 0 출력
# 1 <= n <= 200
# 1 <= k <= 1,000
# 0 <= s <= 10,000

def competitive_spread():
    n, k = map(int, input().split())
    vir_map = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    x -= 1
    y -= 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 초기 바이러스 좌표
    vir_list = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            v = vir_map[i][j]
            if v != 0:
                vir_list[v].append([i, j])

    def print_vir():
        print(f"sec : {sec}, virus : {v}")
        for line in vir_map:
            print(' '.join(map(str, line)))
        print()

    def spread(v, vx, vy):
        for d in range(4):
            nx = vx + dx[d]
            ny = vy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if vir_map[nx][ny] == 0:
                    vir_map[nx][ny] = v
                    vir_list[v].append([nx, ny])

    for sec in range(1, s+1):
        for v in range(1, k+1):
            tmp_list = []
            while vir_list[v]:
                tmp_list.append(vir_list[v].pop())

            while tmp_list:
                vx, vy = tmp_list.pop()
                spread(v, vx, vy)
            print_vir()  #################### 바이러스 맵 출력

    answer = vir_map[x][y]
    print(answer)

competitive_spread()

# input1
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# input2
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2

""" answer solution : BFS 사용 ( 난 못썼음, 알아둘 것 )"""

# BFS 사용 코드 느낀점
# BFS(큐)를 사용하니 매 초마다 현재 바이러스 확산 정도와 다음 바이러스 확산 정도를 분리하여 설계할 필요가 없어짐
# 초기 상태에서 바이러스 종류 순서대로 한번 정렬해주고 큐에 넣은 뒤 정렬된 순서대로 popleft()만 해주면 돼서.
# 내 코드에서는 매 초마다 i번 바이러스 모든 현위치를 vir_list 에서 pop()으로 전부 뽑아 tmp_list에 저장하고,
# tmp_list 에 담긴 위치를 보고 확산시켜 새롭게 확산된 바이러스 위치를 다시 vir_list 에 append() 해주는
# 작업이 추가로 들어감.

def competitive_spread_ans():
    from collections import deque
    n, k = map(int, input().split())
    graph = []  # 전체 맵
    data = []  # 바이러스 정보

    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            # 바이러스가 존재하면
            if graph[i][j] != 0:
                # (바이러스 종류, 시간, x좌표, y좌표) 삽입
                data.append((graph[i][j], 0, i, j))

    # 정렬 이후에 큐로 옮기기
    data.sort()
    q = deque(data)

    target_s, target_x, target_y = map(int, input().split())

    # 바이러스 퍼져나가는 방향
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS 진행
    while q:
        virus, s, x, y = q.popleft()
        # 정확히 s 초가 지나거나, 큐가 빌 때까지 반복
        if s == target_s:
            break
        # 현재 노드에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 위치로 이동할 수 있는 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 아직 방문하지 않은 위치라면 바이러스 넣기
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))

    print(graph[target_x - 1][target_y - 1])

competitive_spread_ans()