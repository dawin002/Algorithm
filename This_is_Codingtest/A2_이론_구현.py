""" 구현 : Implementation """

# 문제에 제시한 사항을 소스코드로 옮기는 과정

# 카테고리
#     완전 탐색
#     시뮬레이션

# 파이썬 리스트의 크기
#     정수      1,000 개 - 4KB
#     정수  1,000,000 개 - 4MB
#     정수 10,000,000 개 - 40MB

# 시간복잡도
#     시간 제한 1초 : 약 20,000,000 회 연산 이내로 풀어야함
#                  데이터 개수 1,000,000 개 기준 O(NlogN) 정도

""" 완전 탐색 """

# 가능한 경우의 수를 모두 검사해보는 탐색 유형
# 일반적으로 비효율적인 시간복잡도 가짐 -> 전체 데이터 개수 100만개 이하일 때 적절


""" 시뮬레이션 """

# 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 유형

# 상하좌우 문제
#     인접 칸을 확인하고 이동하는 문제
#     dx, dy 리스트를 만들고 현재 좌표 x, y 에 더해 다음 좌표 nx, ny 로 이동 가능한지 확인하는 유형

# 시각 문제
#     현재 방향을 기억하고 탐색, 이동하는 문제
#     방향 direction 전역변수를 두고 direction 을 순서에 맞게 회전시키며 이동

#     상  우  하  좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 (0 1 2 3 : 상 우 하 좌)
direction = 0

# 시계방향 회전
def turn_right(direction):
    direction += 1
    if direction == 4:
        direction = 0
    return direction

# 반시계방향 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

count = 0
turn_time = 0

while True:
    # 회전 1회
    direction = turn_left(direction)
    # 다음 좌표 설정
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 다음 좌표 갈 수 있으면
    if 0 <= nx < n and 0 <= ny < m:
        if mmap[nx][ny] == can_move:
            # 현재 좌표 다음 칸으로 이동
            x = nx
            y = ny
            # 밟은 칸 수 += 1
            count += 1
            # 방향 전환 회수 초기화
            turn_time = 0
            # 이동, 반복문 처음으로
            continue
    else:
        turn_time += 1  # 방향 전환 회수 += 1
    # 방향 전환 4번 다 확인했으면
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 뒤로 가기
        if mmap[nx][ny] == can_move:
            x = nx
            y = ny
            turn_time = 0
        else:
            # 이동 불가능, 반복문 탈출
            break