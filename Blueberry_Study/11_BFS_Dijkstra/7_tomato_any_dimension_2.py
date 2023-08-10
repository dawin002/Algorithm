import sys
import heapq

input = sys.stdin.readline  # 백준 제출할 땐 아래 코드로 하기 ( 더 빠르다고 함 )
# input = iter(open(0).read().split('\n')).__next__

# n 차원에 방 몇개씩 있는지 받기
dimensions = list(map(int, input().split()))

# 총 몇차원인지
D_SIZE = len(dimensions)

# 인접한 칸으로 향하는 모든 방향 리스트 생성
direction = [[0 for _ in range(D_SIZE)] for _ in range(D_SIZE * 2)]
for i in range(D_SIZE):
    direction[i][i] = 1
    direction[D_SIZE + i][i] = -1

zero_count = 0  # 안익은 토마토 개수 (0 저장된 칸)
queue = []      # 익은 토마토 큐
position = []   # 큐에 넣을 익은 토마토 칸의 좌표


# 토마토 테이 만들기 ( 몇차원인지 정해져있지 않으니 재귀로 구현 )
def make_table(idx):
    if idx == D_SIZE:
        global zero_count
        line = list(map(int, input().split()))  # 한 줄 입력받기
        # 입력받은 줄의 각 칸 확인하며
        for j in range(len(line)):
            # 익은 토마토는 마지막 차원의 몇번칸인지 확인 후 1(익음)과 좌표 큐에 저장
            if line[j] == 1:
                position.append(j)
                queue.append((1, *position))
                position.pop()
            # 안익은 토마토는 개수 기록
            elif line[j] == 0:
                zero_count += 1
        # 입력받은 (최하위 - 1)차원의 토마토 한 줄 리턴
        return line

    now_tmt_table = []  # 현재 차원의 토마토 테이블

    # 현재 차원의 칸 만큼 반복하며
    for i in range(dimensions[-idx]):
        position.append(i)  # 좌표에 idx 차원의 i번째 칸 추가
        now_tmt_table.append(make_table(idx + 1))  # 다음 차원으로 넘어가기, 리턴된 토마토 테이블 현재 차원에 추가
        position.pop()      # 좌표에서 idx 차원의 i번째 칸 제거

    # 현재 차원의 토마토 테이블 리턴
    return now_tmt_table


# nxt_pos 좌표의 칸에 저장된 값 반환
def get_tomato_value(tmp_tmt_table, idx):
    global nxt_pos
    # 마지막 차원까지 오면 토마토 값 리턴
    if idx == D_SIZE - 1:
        return tmp_tmt_table[nxt_pos[idx]]
    # 다음 차원의 nxt_pos 좌표에 해당하는 테이블을 인자로 재귀 호출, 리턴값 리턴
    return get_tomato_value(tmp_tmt_table[nxt_pos[idx]], idx + 1)


# nxt_pos 좌표의 칸에 새로운 값 저장
def set_tomato_value(tmp_tmt_table, idx, value):
    global nxt_pos
    # 마지막 차원까지 오면 토마토 값 설정
    if idx == D_SIZE - 1:
        tmp_tmt_table[nxt_pos[idx]] = value
        return
    # 다음 차원의 nxt_pos 좌표에 해당하는 테이블을 인자로 넘겨주며 재귀 호출
    set_tomato_value(tmp_tmt_table[nxt_pos[idx]], idx + 1, value)


# 마지막 전 차원에서 readline 으로 받기 때문에 1부터 시작
tomato_table = make_table(1)

# 익은 토마토 저장 배열 우선순위큐로 만들기
heapq.heapify(queue)

while queue:
    # 익은 날짜, 현재 좌표 받아오기
    day, *now_pos = heapq.heappop(queue)

    # 인접한 모든 방향의 칸 확인 및 그 칸의 토마토 익히기
    for dir_pos in direction:
        # 다음 칸의 좌표는 현재칸의 i차원 좌표 + i차원 방향값
        nxt_pos = [now_pos[i] + dir_pos[i] for i in range(len(dir_pos))]

        # 인접 칸 좌표가 전체 테이블의 범위를 벗어나는지 확인
        is_pos_in_range = True
        for i in range(D_SIZE):
            if not (0 <= nxt_pos[i] < dimensions[::-1][i]):
                is_pos_in_range = False
                break

        # 벗어난다면 컨티뉴
        if not is_pos_in_range:
            continue

        # 인접 칸 좌표가 안익은 토마토가 아니면 컨티뉴
        if get_tomato_value(tomato_table, 0) != 0:
            continue

        # nxt_pos 좌표의 토마토 값 갱신
        set_tomato_value(tomato_table, 0, day + 1)

        # 0인 칸이 하나 바뀌었으니 안익은 토마토 1 감소
        zero_count -= 1

        # 갱신된 익은 날짜와 nxt_pos 좌표 큐에 넣기
        heapq.heappush(queue, (day + 1, *nxt_pos))

# 모든 토마토가 익지 않았다면 -1 출력
if zero_count != 0:
    print(-1)
# 모든 토마토가 다 익었다면 day - 1 출력 ( 익은 날짜를 1부터 시작해서 )
else:
    print(day - 1)