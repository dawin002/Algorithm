# bfs로 풀것
# N*N 최대 100

from collections import deque
import sys
sys.stdin = open("D3_F_1244_최대_상금_input.txt", "r")

T = int(input())

def bfs(x, y):
    q = deque()
    q.append([x, y])
    smap[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if mmap[nx][ny] + smap[x][y] < smap[nx][ny]:
                    smap[nx][ny] = mmap[nx][ny] + smap[x][y]
                    q.append([nx, ny])
                    # for a in smap :
                    #     print(' '.join(map(str, a)))
                    # print()
    return smap[N - 1][N - 1]

for test in range(1, T+1) :
    N = int(input())

    mmap = [ list(map(int, input())) for _ in range(N)]
    smap = [[99999]*N for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(f'#{test} {bfs(0,0)}')

# answer
# 1 2
# 2 2
# 3 8
# 4 57
# 5 151
# 6 257
# 7 18
# 8 160
# 9 414
# 10 395
