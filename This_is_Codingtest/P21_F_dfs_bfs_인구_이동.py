""" DFS/BFS 문제 : 21. 인구 이동 """

# n x n 땅
# 각 땅 하나의 나라
# 각 땅 그 나라 인구 수 저장

# 규칙
# 1. 인접 칸 인구 차이 L <= 인구 <= R 이면 국경선 하루 열기
# 2. 국경선 열리면 인구 이동 시작
# 3. 국경선 열려 있는 인접 칸들 = 연합
# 4. 연합 이루는 각 칸 인구 = 연합 전체 인구 // 연합 칸 수
# 5. 연합 해체, 국경선 닫기

# 인구 이동 몇 번 발생 하는지 출력

# start time = 1640

""" my solution : 재귀함수 에러로 실패 """

""" answer solution : BFS 써서 풀어야됨! """

def people_move_ans():
    from collections import deque
    n, l, r = map(int, input().split())

    # 전체 나라별 인구수 입력 받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 특정 위치에서 출발하여 모든 연합을 체크한 뒤 데이터 갱신
    def process(x, y, index):
        # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
        united = []
        united.append((x, y))

        # BFS 를 위한 큐 자료구조 정의
        q = deque()
        q.append((x, y))  # 현재 연합의 첫 번째 국가 좌표
        union[x][y] = index  # 현재 연합의 번호 할당
        summary = graph[x][y]  # 현재 연합의 전체 인구 수
        count = 1  # 현재 연합의 국가 수

        while q:
            x, y = q.popleft()  # 연합 큐에서 한 국가 꺼내서
            for i in range(4):  # 4가지 방향 확인
                nx = x + dx[i]
                ny = y + dy[i]
                # 옆 국가가 지도 범위 안에 있고, 연합 번호가 -1(연합 미포함, not visited 의미)이고,
                if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                    # 현재 국가와의 인구 차이가 l 이상 r 이하 범위 내에 있으면
                    if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                        # 현재 연합 큐에 옆 국가 넣기
                        q.append((nx, ny))
                        # 전체 연합 지도에 현재 연합 번호 표시
                        union[nx][ny] = index           # 얘랑
                        # 현재 연합 전체 인구 수에 더하기
                        summary += graph[nx][ny]
                        # 현재 연합의 국가 수 1 증가
                        count += 1
                        # 현재 연합 리스트에 국가 넣기
                        united.append((nx, ny))

        # 현재 연합 국가들 인구 분배
        for i, j in united:
            graph[i][j] = summary // count              # 얘가 함수 밖으로 나감

    # process(x, y, index) ==> return 없으나,
    # union 리스트 ( 각 국가가 속한 연합 번호로 채운 전체 연합 지도 )
    # graph 리스트 ( 각 국가 인구 수 지도 )
    # 호출 될 때마다 위 두 리스트 갱신 시킴

    total_count = 0

    while True:
        # 국가별 몇 번 연합에 속해 있는지 저장된 리스트 (-1로 초기화)
        union = [[-1] * n for _ in range(n)]
        # 현재 연합 번호
        index = 0
        # 전체 union 리스트 탐색
        for i in range(n):
            for j in range(n):
                # [i][j]번 국가가 속한 연합이 없다면
                if union[i][j] == -1:
                    # [i][j]번 국가와 연결된 모든 국가 index 번으로 연합 번호 세팅, 인구 분배
                    process(i, j, index)
                    # 연합 번호 1 증가
                    index += 1
        # 더 이상 인구 이동이 안일어나는 경우 break
        # : 연합을 거칠수록 인구 수 비슷해지고, 인구 수 비슷해지면 결국 연합을 이루지 않게 됨
        #   결국 모든 국가가 연합을 이루지 않게 되었을 때 while문 종료
        if index == n * n:
            break
        # 최종 연합 이룬 횟수 1 증가
        total_count += 1

    print(total_count)

people_move_ans()

# input1
# 2 20 50
# 50 30
# 20 40

# input2
# 2 40 50
# 50 30
# 20 40

# input3
# 2 20 50
# 50 30
# 30 40

# input4
# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# input5
# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10