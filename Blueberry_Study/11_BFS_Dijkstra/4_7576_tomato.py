import sys
import heapq
input = sys.stdin.readline

m, n = map(int, input().split())
mmap = []
q = []
zero_count = 0

for i in range(n):
    line = list(map(int, input().split()))
    mmap.append(line)
    zero_count += line.count(0)
    for j in range(m):
        if line[j] == 1:
            q.append((1, i, j))

heapq.heapify(q)

while q:
    day, x, y = heapq.heappop(q)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < n and 0 <= ny < m):
            continue
        if mmap[nx][ny] != 0:
            continue
        zero_count -= 1
        mmap[nx][ny] = day + 1
        heapq.heappush(q, (day + 1, nx, ny))

if zero_count != 0:
    print(-1)
else:
    print(day - 1)