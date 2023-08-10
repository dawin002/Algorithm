# 시작칸 : 0,0   끝칸 : N-1,M-1
# 움직칸 : 1,    괴물칸 : 0

""" my code """
from collections import deque

N, M = map(int, input().split())
mmap = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and mmap[nx][ny] == 1:
                mmap[nx][ny] = mmap[x][y]+1
                q.append([nx, ny])
    return mmap[N-1][M-1]

print(bfs(0, 0))

# 결과 맵 출력
# for a in mmap:
#     print(' '.join(map(str, a)))

# 최소값 : 10
#
# Map 결과
#  3  0  5  0  7  0
#  2  3  4  5  6  7
#  0  0  0  0  0  8
# 14 13 12 11 10  9
# 15 14 13 12 11 10
#
# 10 이상의 수가 끝칸에 다시 들어가면 어떡해??
# 그럴 일은 없음. 1인 칸만 확인해서 거리를 수정해주기 때문에
# 그럼 칸에 처음 들어간 거리값이 최소값이 아니면 어떡해?
# bfs 특성상 처음 들어간 값이 가장 작은 값임. 하지만 거리가 1로 고정되지 않은 경우라면 다를지도?