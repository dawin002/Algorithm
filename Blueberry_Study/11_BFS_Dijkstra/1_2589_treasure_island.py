import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    global mmap
    distance = [[-1 for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((x, y))
    distance[x][y] = 0

    maxi = 0

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if distance[nx][ny] != -1:
                continue
            if mmap[nx][ny] == 'W':
                continue
            distance[nx][ny] = distance[x][y] + 1
            maxi = max(maxi, distance[nx][ny])
            q.append((nx, ny))

    return maxi

n, m = map(int, input().split())
mmap = [list(input().rstrip()) for _ in range(n)]

max_dist = 0

for x in range(n):
    for y in range(m):
        if mmap[x][y] == 'W':
            continue
        dist = bfs(x, y)
        max_dist = max(max_dist, dist)

print(max_dist)

