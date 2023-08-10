import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
mmap = [list(input().rstrip()) for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]

max_dist = 0

q = deque()

for sx in range(n):
    for sy in range(m):
        if mmap[sx][sy] == 'W':
            continue

        q.append((sx, sy))
        distance[sx][sy] = 0

        while q:
            x, y = q.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if distance[nx][ny] != -1:
                    continue
                if mmap[nx][ny] == 'W':
                    continue

                distance[nx][ny] = distance[x][y] + 1
                max_dist = max(max_dist, distance[nx][ny])
                q.append((nx, ny))

        for i in range(n):
            for j in range(m):
                distance[i][j] = -1

print(max_dist)