from collections import deque
import sys
input = sys.stdin.readline

sina_x, sina_y, n = map(int, input().split())
sina_x += 500
sina_y += 500

mmap = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
    tmp_x, tmp_y = map(int, input().split())
    mmap[tmp_x + 500][tmp_y + 500] = -1

q = deque()
q.append((500, 500))

while q:
    x, y = q.popleft()
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= 1000 and 0 <= ny <= 1000:
            if mmap[nx][ny] == 0:
                mmap[nx][ny] = mmap[x][y] + 1
                q.append((nx, ny))

    if mmap[sina_x][sina_y] != 0:
        break

print(mmap[sina_x][sina_y])