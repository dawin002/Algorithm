""" DFS/BFS 문제 : 22. 블록 이동하기 """

# 지도 크기 : n x n
# 로봇 크기 : 1 x 2
# 칸 == 0 : 길, 칸 == 1 : 벽
# 목적지 (n, n) 칸에 로봇 한칸이라도 들어가면 도착
# 로봇 회전 : 2 x 2 칸 필요
# 칸 이동 / 90도 회전 시간 : 1초
# 도착하는데 걸리는 최소 시간 리턴
#
# 5 <= n <= 100
# 칸 = 0 or 1
# 무조건 도착 가능한 지도만 제공
#
# input
# [[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,0,0]]

""" answer solution"""

input1 = [[0,0,0,1,1],
          [0,0,0,1,0],
          [0,1,0,1,1],
          [1,1,0,0,1],
          [0,0,0,0,0]]

# 현재 칸에서 다음으로 갈 수 있는 모든 칸 반환
def get_next_pos(pos, board):
    # 현재 칸에서 이동할 수 있는 로봇의 다음 위치 리스트
    next_pos = []
    # pos 집합을 리스트로 바꿈
    pos = list(pos)

    pos1_x = pos[0][0]
    pos1_y = pos[0][1]
    pos2_x = pos[1][0]
    pos2_y = pos[1][1]

    # 4방향(상  하  좌  우) 이동 가능한지 확인
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x = pos1_x + dx[i]
        pos1_next_y = pos1_y + dy[i]
        pos2_next_x = pos2_x + dx[i]
        pos2_next_y = pos2_y + dy[i]
        # 로봇의 다음 위치 두 칸 다 0(빈 칸)이면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            #  next_pos 리스트에 { (pos1좌표), (pos2좌표) } 추가
            #  ... { } 집합 쓰는 이유 : pos1,2 바뀐 중복 안 생기게 하려고
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 로봇 배치가 가로일 때 세로로 회전 가능한지 확인
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            # i = -1일 때 : 위 두 칸이 비었을 때 -> pos1 and 위 쪽으로 회전, pos2 and 위 쪽으로 회전
            # i =  1일 때 : 아래 두 칸이 비었을 때 -> pos1 and 아래 쪽으로 회전, pos2 and 아래 쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y]:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 로봇 배치가 세로일 때 가로로 회전 가능한지 확인
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            # i = -1일 때 : 왼쪽 두 칸이 비었을 때 -> pos1 and 왼 쪽으로 회전, pos2 and 왼 쪽으로 회전
            # i =  1일 때 : 오른쪽 두 칸이 비었을 때 -> pos1 and 오른 쪽으로 회전, pos2 and 오른 쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 이동할 수 있는 모든 위치가 담긴 next_pos 리스트 반환
    return next_pos

def move_block(board):
    from collections import deque
    # 맵의 외곽에 벽을 한 겹 두른 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # BFS 수행
    q = deque()
    visited = []

    pos = {(1, 1), (1, 2)}
    # 현재 위치 큐에 넣고 방문 처리
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        # 로봇이 (n, n) 위치에 도달했다면 최단거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는지 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 넣고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0

answer = move_block(input1)
print(answer)