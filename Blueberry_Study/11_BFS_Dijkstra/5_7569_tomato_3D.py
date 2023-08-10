import sys
import heapq

input = sys.stdin.readline

m, n, h = map(int, input().split())
mmap = [[] for _ in range(h)]
q = []
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
zero_count = 0

for k in range(h):
    for i in range(n):
        line = list(map(int, input().split()))
        mmap[k].append(line)
        zero_count += line.count(0)
        for j in range(m):
            if line[j] == 1:
                q.append((1, i, j, k))

heapq.heapify(q)

while q:
    day, x, y, z = heapq.heappop(q)
    for dx, dy, dz in direction:
        nx, ny, nz = x + dx, y + dy, z + dz
        if not (0 <= nx < n and 0 <= ny < m and 0 <= nz < h):
            continue
        if mmap[nz][nx][ny] != 0:
            continue
        zero_count -= 1
        mmap[nz][nx][ny] = day + 1
        heapq.heappush(q, (day + 1, nx, ny, nz))

if zero_count != 0:
    print(-1)
else:
    print(day - 1)
